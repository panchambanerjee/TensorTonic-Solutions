-- Write your SQL query here
SELECT u.username, e.experiment_name, e.variant, c.revenue
FROM users u
JOIN experiment_assignments e ON u.id = e.user_id
JOIN conversions c ON u.id = c.user_id
ORDER BY e.experiment_name ASC, c.revenue DESC, u.username ASC;