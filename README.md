# Sales Dashboard | Excel, Python, Pandas, SQL & Power BI

## Project overview
A sales analytics portfolio project exploring sales performance, profit, product performance, customer purchasing patterns, payment methods and regional results.

## Dashboard pages
- **Home:** KPI cards, revenue trend, category-wise profit, region-wise sales and payment methods.
- **Sales:** monthly sales trend, region comparison, top-selling products and category mix.
- **Customer:** top customers, customer segments and monthly purchase trends.
- **Product:** top- and under-performing products and category performance.
- **Profit:** profit margin, regional profit and product profitability.

## Tools
- Excel — inspection and basic data cleaning
- Python and Pandas — data validation, transformation and export
- SQL — KPI calculations, group-by analysis and quality checks
- Power BI — interactive dashboard and visual reporting

## Repository files
- `sales_data_raw_sample.csv` — synthetic sample data with a few intentional quality issues for practice.
- `python_pandas_cleaning.py` — end-to-end cleaning script.
- `pandas_cleaning_commands.txt` — separate Pandas command reference.
- `python_commands.txt` — basic Python commands used.
- `excel_data_cleaning_guide.xlsx` — Excel cleaning checklist.
- `sql_analysis.sql` — SQL checks and analysis queries.
- `screenshots/` — dashboard screenshots.

## How to run
1. Install Python 3 and Pandas: `pip install pandas`
2. Put `sales_data_raw_sample.csv` and `python_pandas_cleaning.py` in the same folder.
3. Run: `python python_pandas_cleaning.py`
4. The script creates `sales_data_cleaned.csv`.
5. Import the cleaned CSV into Power BI and build/refresh visuals.
6. Run the SQL examples after importing the data into a database and adjusting the table/column types as needed.

## Data note
The included CSV is **synthetic sample data generated for demonstration**. It is not claimed to be the original dataset behind the supplied dashboard screenshots. Replace it with the real source data if available, and rerun validation before publishing results.

## Important quality checks
- Verify duplicate order IDs and missing key fields.
- Confirm dates and numeric data types.
- Check that Sales = Quantity × Unit_Price.
- Confirm the business definition of Profit and Profit Margin.
- Compare Power BI totals against SQL/Excel totals.

## Suggested GitHub description
Sales analytics dashboard built with Power BI, supported by Excel, Python/Pandas data cleaning and SQL analysis.
