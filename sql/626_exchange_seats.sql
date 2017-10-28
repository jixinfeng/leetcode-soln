/*
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat.
*/
# Write your MySQL query statement below
SELECT p1.id, IF(
    p1.id % 2 = 0, 
    (SELECT p2.student FROM seat AS p2 WHERE p2.id = p1.id - 1),
    IF (
        p1.id % 2 = 1 and p1.id + 1 in (SELECT id FROM seat), 
        (SELECT p3.student FROM seat AS p3 WHERE p3.id = p1.id + 1),
        p1.student
    )
) AS student
FROM seat AS p1
