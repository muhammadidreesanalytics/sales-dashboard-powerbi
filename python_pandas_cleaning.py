"""
Sales Dashboard project: data cleaning with Python and Pandas.
Input: sales_data_raw_sample.csv
Output: sales_data_cleaned.csv
Note: this repository's included data is synthetic sample data.
"""
import pandas as pd

INPUT_FILE = "sales_data_raw_sample.csv"
OUTPUT_FILE = "sales_data_cleaned.csv"

# 1. Load data
df = pd.read_csv(INPUT_FILE)
print("Raw shape:", df.shape)
print(df.head())

# 2. Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# 3. Remove duplicate order IDs (keep first occurrence)
df = df.drop_duplicates(subset=["order_id"], keep="first")

# 4. Clean text columns: trim spaces and standardize capitalization where appropriate
text_cols = ["customer_name", "product_name", "category", "region", "city", "payment_method"]
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

df["region"] = df["region"].str.title()
df["city"] = df["city"].str.title()
df["payment_method"] = df["payment_method"].str.title()

# 5. Convert data types safely
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
numeric_cols = ["quantity", "unit_price", "sales", "profit"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 6. Handle missing values
df = df.dropna(subset=["order_id", "customer_name", "product_name", "order_date"])
df = df.dropna(subset=["quantity", "unit_price"])
df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]

# 7. Recalculate sales from quantity and unit price to avoid inconsistent totals
df["sales"] = df["quantity"] * df["unit_price"]

# 8. Validate profit; missing profit is set to 0 here, but in a real project confirm business rules
df["profit"] = df["profit"].fillna(0)
df = df[df["profit"] >= 0]

# 9. Add useful analytical columns
df["month"] = df["order_date"].dt.month_name()
df["year"] = df["order_date"].dt.year
df["profit_margin_pct"] = (df["profit"] / df["sales"] * 100).where(df["sales"] != 0, 0).round(2)

# 10. Export clean dataset
df.to_csv(OUTPUT_FILE, index=False)
print("Cleaned shape:", df.shape)
print("Missing values by column:\n", df.isna().sum())
print("Duplicate order IDs:", df["order_id"].duplicated().sum())
print(f"Saved cleaned file: {OUTPUT_FILE}")
