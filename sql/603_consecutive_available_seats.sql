/*
Several friends at a cinema ticket office would like to reserve consecutive
available seats.

Can you help to query all the consecutive available seats order by the seat_id
using the following cinema table?

| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |

Your query should return the following result for the sample case above.

| seat_id |
|---------|
| 3       |
| 4       |
| 5       |

Note:
The seat_id is an auto increment int, and free is bool ('1' means free, and '0'
means occupied.).  Consecutive available seats are more than 2(inclusive)
seats consecutively available.
*/
SELECT DISTINCT b.seat_id
FROM cinema AS a, cinema AS b, cinema AS c
WHERE (
    a.seat_id = b.seat_id - 1 AND a.free = 1 AND b.free = 1
) 
OR (
    b.seat_id = c.seat_id - 1 AND b.free = 1 AND c.free = 1
)
ORDER BY b.seat_id;
