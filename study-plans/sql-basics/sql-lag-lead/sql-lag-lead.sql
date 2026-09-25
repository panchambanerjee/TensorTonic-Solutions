-- Write your SQL query here
SELECT month, revenue, 
 LAG(revenue, 1, 0) OVER (ORDER BY month) AS prev_revenue,
 revenue - prev_revenue AS revenue_change
FROM monthly_revenue
ORDER BY month ASC;