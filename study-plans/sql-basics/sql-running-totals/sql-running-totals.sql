SELECT account, txn_date, amount,
       SUM(amount) OVER (
         PARTITION BY account
         ORDER BY txn_date, id
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM transactions
ORDER BY account ASC, txn_date ASC, id ASC;
