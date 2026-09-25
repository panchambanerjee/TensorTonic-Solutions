-- Write your SQL query here
SELECT name, price, 
 ROUND(products.price - (SELECT AVG(price) FROM products), 2) AS vs_avg
FROM products 
WHERE products.id IN ( SELECT product_id FROM sales)
ORDER BY vs_avg DESC, name ASC;