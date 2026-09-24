-- Write your SQL query here
SELECT 
DISTINCT customer_name , COUNT(DISTINCT product) as unique_products
FROM orders
GROUP BY customer_name
ORDER BY unique_products DESC, customer_name ASC;