-- Write your SQL query here
SELECT category, COUNT(*) AS total_sales,
SUM(amount) AS total_revenue, ROUND(AVG(discount), 2) AS avg_discount
FROM sales
GROUP BY category
ORDER BY total_revenue DESC, category ASC;