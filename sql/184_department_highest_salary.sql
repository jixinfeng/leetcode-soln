/*
The Employee table holds all employees. Every employee has an Id, a salary, and
there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the
departments. For the above tables, Max has the highest salary in the IT
department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/
# Write your MySQL query statement below
SELECT S.Department, E.Name AS Employee, E.Salary
FROM Employee AS E, (
    SELECT D.Id AS Id, D.Name AS Department, MAX(E.Salary) AS MaxSalary
    FROM Department AS D, Employee AS E
    WHERE E.Departmentid = D.Id
    GROUP BY D.Id
) AS S
WHERE E.DepartmentId = S.Id AND E.Salary = S.MaxSalary
ORDER BY E.Salary DESC;
