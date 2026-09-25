-- Write your SQL query here
WITH customer_summary AS 
    (
    SELECT customer, COUNT(*) AS order_count, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer
    )

SELECT customer, order_count, total_spent
FROM customer_summary
WHERE order_count > 1
ORDER BY total_spent DESC, customer ASC;