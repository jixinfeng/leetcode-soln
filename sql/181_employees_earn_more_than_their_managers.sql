# Write your MySQL query statement below
SELECT E.Name AS Employee 
FROM Employee AS E, Employee AS B 
WHERE E.ManagerId = B.Id AND E.Salary > B.Salary;
