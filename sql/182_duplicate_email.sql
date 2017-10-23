# Write your MySQL query statement below
SELECT Email 
FROM (
    SELECT Email, COUNT(*) AS ct FROM Person GROUP BY Email
) AS EmailCt 
WHERE ct > 1;
