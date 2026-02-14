# Shopping_Behavior Data Analysis with Python and Excel

## 📚 Table of Contents
- [1. Overview](#1-Overview)
- [2. Dataset Information](#2-dataset-information)
- [3. Objectives](#3-objectives)
- [4. Tools & Technologies](#4-tools--technologies)
- [5. Project Structure](#5-project-structure)
- [6. Steps / Workflow](#6-steps--workflow)
- [7. Key Insights](#7-key-insights)
- [8. Visualizations](#8visualizations)
- [9. How to Run the Project](#9-how-to-run-the-project)
- [10. Future Improvements](#10-future-improvements)
- [Quick Links](#quick-links)
- [Contact](#contact)


## 1. Overview 
The project includes the EDA of the “Shopping behaviour dataset”. It contains data cleaning and preprocessing Python scripts and an analysis ipynb file. The cleaned data was then effectively transformed and visualized using the Matplotlib and Seaborn libraries. Custom aggregations, such as mean, median, and distribution plots of review scores, provided deeper insights.

Contains:
    - State-wise Review Analysis : Aggregates customer ratings across states and seasons.  
    - Trend Visualization : Displays seasonal shifts in consumer sentiment.
    - Interactive Geomap : Choropleth map showing average ratings per state.
    - Custom Aggregations : Mean, median, and distribution plots of review scores.
    - Interactive Dashboard : Excel-based KPIs, pivots, and geomaps for quick insights.


## 2. Dataset Information
    [Dataset](https://www.kaggle.com/datasets/zubairdhuddi/shopping-dataset)

    - The dataset is sourced from Kaggle’s Customer Shopping Trends Dataset. It captures detailed customer-level transactional and behavioral information, making it an excellent resource for exploratory data analysis, customer segmentation, and predictive modeling tasks. 
    - The dataset contains a total of 3,900 individual transactions and includes 18 original features that describe various aspects of customer purchases and preferences. During preprocessing and analysis (both in Python scripts and Excel), several additional derived features were created to enhance insights and support deeper segmentation. The data is structured in a tabular format, available as both CSV and XLSX files, and belongs to the retail, e-commerce, and customer analytics domain.

    -List or describe important features:  
        - Customer ID - Unique identifier for each customer
        - Age - Customer’s age
        - Gender - Male/Female/Other
        - Item Purchased - Product bought
        - Category - Item category (e.g., Clothing, Electronics)
        - Purchase Amount (USD) - Transaction value of the item purchased
        - Location - City or region of the customer
        - Size - Size of the purchased item (e.g., S, M, L, XL)
        - Color - Color of the purchased item
        - Season - Season during which the purchase was made (e.g., Winter, Spring)
        - Review Rating - Feedback score (typically 1–5)
        - Subscription Status - Whether the customer is subscribed (Yes/No)
        - Shipping Type - Delivery method (e.g., Express, Free Shipping)
        - Discount Applied - Whether a discount was applied (Yes/No)
        - Promo Code Used - Whether a promo code was used (Yes/No)
        - Previous Purchases - Number or value of previous purchases made by the customer
        - Payment Method -Mode of payment (e.g., Card, Cash, UPI)
        - Frequency of Purchases - How often the customer shops (e.g., Daily, Weekly, or numeric frequency)


## 3. Objectives
    1. Identifing the insights of datset.
    2. Relation between the Previous and current purchases.
    3. Identifing purchase of items per Geological location.
    4. Overall exploration of shopping behaviour dataset.
    5. Estimate the future sales items.


## 4. Tools & Technologies
- Language: Python , Excel
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- IDE: Jupyter Notebook / VS Code
- Visualization: Excel
        
## 5. Project Structure

shopping-behavior-analysis/
├── data/
│   └── shopping_behavior.csv   
├── notebooks/
│   └── Analysis.ipynb                 
├── scripts/
│   ├── preprocess.py     
│   └── analysis.py                  
├── outputs/
│   ├── plots/                          
│   └── reports/    
├── dashboard/
│   └── shopping_behavior_updated.xlsx
├── images/                        
├── README.md
├── .gitignore
└── requirements.txt


## 6. Steps / Workflow
    1. Data Cleaning and exploration : Handle missing values, duplicates, and outliers.
    2. Exploratory Data Analysis (EDA) : Analyze numerical and categorical patterns also describe the co-relation of data intent.
    3. Visualization : Create graphs for spending trends in items purchased, age distribution, previous and newly purchased rates comparison , etc.
    4. Insights & Interpretation : Interpret findings to support decisions form the data trends.
    5. Dashboard : Build an interactive summary in Excel. 
    6. Reporting : Summarize findings in outputs/reports/.


## 7. Key Insights
    1. Customers aged ** 25–35 ** years made the most purchases.
    2. Clothing and Electronics categories dominated overall sales.
    3. Seasonal trends affect items purchased rates.
    4. Subscription members spent approximately 30% more on average.
    5. Card payments were the most preferred transaction mode.
    6. Weekends showed a noticeable spike in purchase activity.
    7. Items purchased frequency relate to colors, gender and age.
    8. Profit earned through the items sell compared to previous purchased.
    9. Medium sized Clothing are largely purchased.
    10. Paypal transaction is commonly used mathod for payment.
    11. Repeat customers form a strong revenue segment.
    12. Discount and promo interactions influence purchase behavior.
    13. Some high-revenue categories show lower average ratings — opportunity for improvement.


## 8.Visualizations
    1. Age Distribution of Customers.
    2. Category vs. Total Revenue.
    3. Gender-based Spending Patterns.
    4. Subscription Status vs. Average Spending.
    5. Purchase Trends.
    6. Total Sales , Previous Purchased , Total Purchased in USD , and Earned total Profit.
    7. Payment method variation in used for transaction according to items purchased.
    8. Size vs. items purchased.
    9. Geomap distrbution of items sold and profit Earned.
    10. data co-relation through heatmap.


## 9. How to Run the Project
    1. Clone the repository:
        git clone https://github.com/Hemantdhake/shopping-behavior-data-analysis-with-excel-dashboard.git
        cd shopping-behavior-data-analysis-with-excel-dashboard

    2. Set Up Environment:
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate

    3. Install dependencies:
        pip install -r requirements.txt

    4. Preprocess Data and Run Analysis:
        python scripts/preprocess.py
        python scripts/analysis.py

    5. Launch Jupyter Notebook:
        jupyter notebook Analysis.ipynb

    6. Open Dashboard.xlsx to explore visual insights.


## 10. Future Improvements
    - Integrate Power BI for dynamic dashboards.
    - Implement customer segmentation using clustering algorithms.
    - K-Means clustering for segmentation, regression for purchase prediction.
    - Create a model to predict the sales in purchased of items by season
    - Predict customer churn and potential spend using ML models.
    - Automate weekly data updates from live databases.
    - Rating based suggestion for selecting best items to purchased
    - Add rating-based item suggestions.


## Quick Links:

- 📄 Dataset	`./Dataset/shopping_behavior.csv`
- 📓 Notebook	`./notebook/Analysis.ipynb`
- 📊 Dashboard	`./dashboard/shopping_behavior_updated.xlsx`
- 🧾 Requirements	`./requirements.txt`


## Contact : 
- Author: Hemant Dhake
- 🔗[LinkedIn](https://www.linkedin.com/in/hemant-dhake-4606a8301/)

        