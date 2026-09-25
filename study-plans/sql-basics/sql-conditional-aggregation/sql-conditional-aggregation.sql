-- Write your SQL query here
SELECT department,
       COUNT(*) AS total_tickets,
       SUM(CASE WHEN status = 'open' THEN 1 ELSE 0 END) AS open_count,
       SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) AS in_progress_count,
       SUM(CASE WHEN status = 'closed' THEN 1 ELSE 0 END) AS closed_count
FROM tickets
GROUP BY department
ORDER BY total_tickets DESC, department ASC;
