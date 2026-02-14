import logging
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



def load_data(file_path: str) -> pd.DataFrame:
    # Load CSV with better dtype inference and memory optimization.
    try:
        # Use explicit dtypes where we know the schema → saves memory & prevents surprises
        dtype_spec = {
            "Customer ID": "int32",
            "Age": "int8", # age 18–99 → int8 is enough
            "Gender": "category",
            "Item Purchased": "category",
            "Category": "category",
            "Purchase Amount (USD)": "int16", # 20–100 range
            "Location": "category",
            "Size": "category",
            "Color": "category",
            "Season": "category",
            "Review Rating": "float32",
            "Subscription Status": "category",
            "Shipping Type": "category",
            "Discount Applied": "category",
            "Promo Code Used": "category",
            "Previous Purchases": "int16",
            "Payment Method": "category",
            "Frequency of Purchases": "category"
        }

        df = pd.read_csv(
            file_path,
            dtype=dtype_spec,
            parse_dates=False,  # no real dates in this dataset
            low_memory=False
        )
        logger.info(f"Loaded dataset with shape: {df.shape}")
        return df

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Advanced cleaning with type-aware missing value handling.
    original_shape = df.shape

    # 1. Remove exact duplicates
    df = df.drop_duplicates()
    logger.info(f"Removed {original_shape[0] - df.shape[0]} duplicate rows")

    # 2. Missing values – strategy per column type
    missing_before = df.isna().sum().sum()

    # Numeric columns → median (robust to outliers)
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Categorical columns → mode (most frequent)
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        if df[col].isna().any():
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            logger.debug(f"Filled {col} missing values with mode: {mode_val}")

    missing_after = df.isna().sum().sum()
    logger.info(f"Managed {missing_before - missing_after} missing values")

    return df


def detect_and_handle_outliers(
    df: pd.DataFrame,
    columns: list[str],
    method: str = "iqr",
    threshold: float = 1.5,
    action: str = "cap"
) -> pd.DataFrame:
    # Handle outliers in numeric columns using IQR or z-score.
    df_out = df.copy()

    for col in columns:
        if col not in df_out.columns:
            continue

        series = df_out[col].dropna()

        if method == "iqr":
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - threshold * IQR
            upper = Q3 + threshold * IQR

            mask = (series < lower) | (series > upper)
            outlier_count = mask.sum()

            if outlier_count > 0:
                if action == "cap":
                    df_out.loc[df_out[col] < lower, col] = lower
                    df_out.loc[df_out[col] > upper, col] = upper
                elif action == "remove":
                    df_out = df_out[~mask]
                logger.info(f"{col}: capped/removed {outlier_count} outliers (method={method})")

    return df_out


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    # Create richer features suitable for EDA and modeling.
    df = df.copy()

    # 1. Age grouping (more granular + ordinal encoding option)
    if "Age" in df.columns:
        bins = [0, 18, 25, 35, 45, 55, 65, 100]
        labels = ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
        df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)
        # Optional: ordinal encoding
        df["Age_Group_Ordinal"] = df["Age_Group"].cat.codes

    # 2. Purchase value categories
    if "Purchase Amount (USD)" in df.columns:
        bins = [-np.inf, 30, 50, 75, 100, np.inf]
        labels = ["Very Low", "Low", "Medium", "High", "Very High"]
        df["Purchase_Category"] = pd.cut(
            df["Purchase Amount (USD)"],
            bins=bins,
            labels=labels
        )

    # 3. Discount & Promo interaction
    if all(col in df.columns for col in ["Discount Applied", "Promo Code Used"]):
        df["Discount_or_Promo"] = (
            (df["Discount Applied"] == "Yes") |
            (df["Promo Code Used"] == "Yes")
        ).map({True: "Yes", False: "No"}).astype("category")

    # 4. Loyalty / recency proxy
    if "Previous Purchases" in df.columns:
        df["Is_Repeat_Customer"] = (df["Previous Purchases"] >= 10).astype("int8")

    # 5. Season + Category interaction (popular combos)
    if all(col in df.columns for col in ["Season", "Category"]):
        df["Season_Category"] = df["Season"].astype(str) + "_" + df["Category"].astype(str)

    logger.info("Feature engineering completed. New columns added.")
    return df


def encode_categorical(
    df: pd.DataFrame,
    cols_onehot: Optional[list[str]] = None,
    cols_label: Optional[list[str]] = None,
    drop_first: bool = True
) -> Tuple[pd.DataFrame, dict]:
    # Encoding categorical variables – label & one-hot.
    df_enc = df.copy()
    encoders = {}

    # Label Encoding
    if cols_label:
        for col in cols_label:
            if col in df_enc.columns:
                le = LabelEncoder()
                df_enc[col] = le.fit_transform(df_enc[col].astype(str))
                encoders[col] = le

    # One-Hot Encoding
    if cols_onehot:
        ohe = OneHotEncoder(sparse_output=False, drop="first" if drop_first else None,
                            handle_unknown="ignore")
        ohe_data = ohe.fit_transform(df_enc[cols_onehot])
        ohe_cols = ohe.get_feature_names_out(cols_onehot)
        ohe_df = pd.DataFrame(ohe_data, columns=ohe_cols, index=df_enc.index)
        df_enc = pd.concat([df_enc.drop(columns=cols_onehot), ohe_df], axis=1)
        encoders["onehot"] = ohe

    return df_enc, encoders


def preprocess_pipeline(
    file_path: str,
    handle_outliers: bool = True,
    outlier_method: str = "iqr",
    encode_categoricals: bool = False,
    onehot_cols: Optional[list] = None,
    label_cols: Optional[list] = None
) -> pd.DataFrame:
    # Full production-ready preprocessing pipeline.
    logger.info("Starting preprocessing pipeline...")

    df = load_data(file_path)
    df = clean_data(df)

    # outlier handling
    if handle_outliers:
        numeric_to_check = ["Purchase Amount (USD)", "Previous Purchases", "Age", "Review Rating"]
        present_cols = [c for c in numeric_to_check if c in df.columns]
        df = detect_and_handle_outliers(df, present_cols, method=outlier_method)

    df = feature_engineering(df)

    if encode_categoricals:
        df, _ = encode_categorical(
            df,
            cols_onehot=onehot_cols,
            cols_label=label_cols
        )

    logger.info(f"Preprocessing complete. Final shape: {df.shape}")
    return df


if __name__ == "__main__":
    FILE = "C:\\Users\\Hemant\\Desktop\\Shopping Behavior\\Dataset\\shopping_behavior.csv"  

    processed = preprocess_pipeline(
        FILE,
        handle_outliers=True,
        encode_categoricals=False, 
        onehot_cols=["Gender", "Category", "Season", "Size", "Payment Method"],
        label_cols=["Subscription Status", "Discount Applied", "Promo Code Used"]
    )

    print(processed.head())
    print("\nColumns after preprocessing:")
    print(processed.columns.tolist())