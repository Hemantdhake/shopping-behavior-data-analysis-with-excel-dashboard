import logging
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("muted")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Output directories
OUTPUT_DIR = Path("C:\\Users\\Hemant\\Desktop\\Shopping Behavior\\outputs\\plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def usd_formatter(x, pos):
    # Format numbers as USD with K/M suffix when large.
    if x >= 1e6:
        return f"${x/1e6:.1f}M"
    elif x >= 1e3:
        return f"${x/1e3:.1f}K"
    return f"${x:.0f}"

# Overview
def print_dataset_overview(df: pd.DataFrame) -> None:
    logger.info("Dataset Overview")
    print(f"Shape:  {df.shape}")
    print(f"Memory usage:  {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("\nData Types:")
    print(df.dtypes.value_counts().to_string())
    print("\nMissing Values:")
    miss = df.isna().sum()
    print(miss[miss > 0].to_string() if miss.sum() > 0 else "None")
    print("\nUnique counts (top 10):")
    print(df.nunique().sort_values(ascending=False).head(10).to_string())


def plot_gender_distribution(df: pd.DataFrame, save: bool = True) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))

    sns.countplot(data=df, x="Gender", ax=ax, order=df["Gender"].value_counts().index)

    total = len(df)
    for p in ax.patches:
        count = p.get_height()
        pct = count / total * 100
        ax.annotate(f"{count}\n({pct:.1f}%)",
                    (p.get_x() + p.get_width() / 2., count),
                    ha="center", va="center",
                    xytext=(0, 10), textcoords="offset points",
                    fontsize=10, fontweight="bold")

    ax.set_title("Gender Distribution", fontsize=14, pad=15)
    ax.set_xlabel("Gender", fontsize=11)
    ax.set_ylabel("Number of Customers", fontsize=11)
    ax.tick_params(axis="both", labelsize=10)

    if save:
        plt.savefig(OUTPUT_DIR / "gender_distribution.png", dpi=300, bbox_inches="tight")
        logger.info("Saved: gender_distribution.png")
    plt.close()


def plot_top_categories_by_revenue(
    df: pd.DataFrame,
    top_n: int = 8,
    save: bool = True
) -> None:
    revenue = df.groupby("Category", observed=True)["Purchase Amount (USD)"].sum() \
                .sort_values(ascending=False) \
                .head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = sns.barplot(x=revenue.values, y=revenue.index, ax=ax, palette="viridis")

    ax.xaxis.set_major_formatter(FuncFormatter(usd_formatter))

    for bar in bars.patches:
        width = bar.get_width()
        ax.text(width + 0.02 * width, bar.get_y() + bar.get_height() / 2,
                f"${width:,.0f}", va="center", fontsize=10, fontweight="medium")

    ax.set_title(f"Top {top_n} Categories by Total Revenue", fontsize=15, pad=15)
    ax.set_xlabel("Total Revenue (USD)", fontsize=12)
    ax.set_ylabel("Category", fontsize=12)
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    plt.tight_layout()
    if save:
        plt.savefig(OUTPUT_DIR / "top_categories_revenue.png", dpi=300, bbox_inches="tight")
        logger.info("Saved: top_categories_revenue.png")
    plt.close()


def plot_age_vs_spending_with_trend(
    df: pd.DataFrame,
    save: bool = True
) -> None:
    # Scatter + regression line + marginal distributions.
    fig = plt.figure(figsize=(10, 8))

    # Main scatter + trend
    ax_main = plt.subplot2grid((4, 4), (1, 0), colspan=3, rowspan=3)
    sns.regplot(
        data=df, x="Age", y="Purchase Amount (USD)",
        scatter_kws={"alpha": 0.4, "s": 40},
        line_kws={"color": "darkred", "lw": 2.5},
        ax=ax_main
    )
    ax_main.set_title("Age vs Purchase Amount with Trend Line", fontsize=14)
    ax_main.set_xlabel("Age", fontsize=11)
    ax_main.set_ylabel("Purchase Amount (USD)", fontsize=11)

    # Top marginal (age distribution)
    ax_top = plt.subplot2grid((4, 4), (0, 0), colspan=3, rowspan=1, sharex=ax_main)
    sns.histplot(df["Age"], kde=True, ax=ax_top, color="teal")
    ax_top.set_title("Age Distribution", fontsize=11)
    ax_top.set_xlabel("")
    ax_top.set_ylabel("Count")

    # Right marginal (spending distribution)
    ax_right = plt.subplot2grid((4, 4), (1, 3), colspan=1, rowspan=3, sharey=ax_main)
    sns.histplot(df["Purchase Amount (USD)"], kde=True, ax=ax_right, color="coral",
                 orientation="horizontal")
    ax_right.set_title("Spending Distribution", fontsize=11)
    ax_right.set_ylabel("")
    ax_right.set_xlabel("Count")

    plt.tight_layout()
    if save:
        plt.savefig(OUTPUT_DIR / "age_vs_spending_with_trend.png", dpi=300, bbox_inches="tight")
        logger.info("Saved: age_vs_spending_with_trend.png")
    plt.close()


def plot_average_rating_by_category(df: pd.DataFrame, save: bool = True) -> None:
    # Average review rating per category + count annotation.
    rating_summary = df.groupby("Category", observed=True).agg(
        Avg_Rating=("Review Rating", "mean"),
        Count=("Review Rating", "count")
    ).sort_values("Avg_Rating", ascending=False)

    fig, ax = plt.subplots(figsize=(9, 6))

    bars = sns.barplot(
        x=rating_summary.index,
        y=rating_summary["Avg_Rating"],
        ax=ax,
        palette="coolwarm"
    )

    for i, bar in enumerate(bars.patches):
        height = bar.get_height()
        count = rating_summary["Count"].iloc[i]
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.05,
                f"{height:.2f}\n(n={count})",
                ha="center", va="bottom", fontsize=9, fontweight="medium")

    ax.set_title("Average Review Rating by Category", fontsize=14, pad=15)
    ax.set_xlabel("Category", fontsize=11)
    ax.set_ylabel("Average Rating (1–5)", fontsize=11)
    ax.set_ylim(0, 5.5)
    ax.tick_params(axis="x", rotation=45)

    if save:
        plt.savefig(OUTPUT_DIR / "avg_rating_by_category.png", dpi=300, bbox_inches="tight")
        logger.info("Saved: avg_rating_by_category.png")
    plt.close()


def run_full_analysis(
    file_path: str,
    save_plots: bool = True,
    show_plots: bool = False
) -> None:

    # Execute complete EDA pipeline.
    logger.info("Starting full shopping behavior analysis...")

    # Load data
    try:
        df = pd.read_csv(file_path, low_memory=False)
        logger.info(f"Dataset loaded – {df.shape[0]:,} rows, {df.shape[1]} columns")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return


    print_dataset_overview(df)
    # Visualizations 
    plot_gender_distribution(df, save=save_plots)
    plot_top_categories_by_revenue(df, top_n=8, save=save_plots)
    plot_age_vs_spending_with_trend(df, save=save_plots)
    plot_average_rating_by_category(df, save=save_plots)

    logger.info("Analysis completed.")
    if save_plots:
        logger.info(f"All plots saved to: {OUTPUT_DIR.resolve()}")
    if show_plots:
        plt.show()


if __name__ == "__main__":
    DATA_PATH = "C:\\Users\\Hemant\\Desktop\\Shopping Behavior\\Dataset\\shopping_behavior.csv" 

    run_full_analysis(
        file_path=DATA_PATH,
        save_plots=True,
        show_plots=False
    )