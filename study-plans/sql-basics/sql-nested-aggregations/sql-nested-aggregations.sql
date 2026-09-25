-- Write your SQL query here
WITH daily_sums AS (
    SELECT order_date, COUNT(*) AS daily_count, SUM(amount) AS daily_total
    FROM orders
    GROUP BY order_date
) 

SELECT (ROUND(AVG(daily_count), 2)) AS avg_daily_orders,
(ROUND(AVG(daily_total), 2)) AS avg_daily_revenue,
MAX(daily_count) AS busiest_day_orders
FROM daily_sums