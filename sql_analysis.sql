-- Sales Dashboard: SQL analysis examples
-- Assumed table name: sales_data
-- Adjust column names/types to match your imported table.

-- 1. Check row count
SELECT COUNT(*) AS total_rows FROM sales_data;

-- 2. Check duplicate Order_IDs
SELECT Order_ID, COUNT(*) AS record_count
FROM sales_data
GROUP BY Order_ID
HAVING COUNT(*) > 1;

-- 3. Check missing key fields
SELECT
  SUM(CASE WHEN Customer_Name IS NULL OR TRIM(Customer_Name) = '' THEN 1 ELSE 0 END) AS missing_customers,
  SUM(CASE WHEN Order_Date IS NULL THEN 1 ELSE 0 END) AS missing_dates
FROM sales_data;

-- 4. KPI summary
SELECT
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit,
  COUNT(DISTINCT Order_ID) AS total_orders,
  COUNT(DISTINCT Customer_Name) AS total_customers,
  ROUND(100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0), 2) AS profit_margin_pct
FROM sales_data;

-- 5. Sales by region
SELECT Region, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Region
ORDER BY total_sales DESC;

-- 6. Sales by category
SELECT Category, SUM(Sales) AS total_sales, SUM(Profit) AS total_profit
FROM sales_data
GROUP BY Category
ORDER BY total_sales DESC;

-- 7. Top 5 products by sales
SELECT Product_Name, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Product_Name
ORDER BY total_sales DESC
LIMIT 5;

-- 8. Monthly trend (MySQL)
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS sales_month, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY sales_month;
