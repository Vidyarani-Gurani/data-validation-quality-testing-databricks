-- Null value validation
SELECT COUNT(*) AS null_email_count
FROM sample_customer_data
WHERE email IS NULL;

-- Duplicate customer_id validation
SELECT customer_id, COUNT(*) AS duplicate_count
FROM sample_customer_data
GROUP BY customer_id
HAVING COUNT(*) > 1;
