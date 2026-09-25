-- Write your SQL query here
SELECT 
LOWER(TRIM(respondent)) AS respondent_clean,
LENGTH(TRIM(raw_answer)) AS answer_length,
SUBSTRING(TRIM(raw_answer), 1, 20) AS answer_preview,
SPLIT_PART(source_url, '/', 3) AS source_domain
FROM survey_responses
ORDER BY respondent_clean ASC;