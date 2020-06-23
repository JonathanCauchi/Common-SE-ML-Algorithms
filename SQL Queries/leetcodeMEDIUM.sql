-- 626. Exchange Seats

SELECT 
(CASE
    WHEN id % 2 != 0 and count != id THEN id + 1
    WHEN id % 2 != 0 and count = id THEN id
    ELSE id - 1
END) as id, student
FROM seat, 
(
    SELECT COUNT(*) as count FROM seat
) as seat_count
ORDER BY id ASC;

-- 177. Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
        SELECT DISTINCT(Salary) FROM Employee
        order by Salary 
        LIMIT 1 offset N
     );
END

-- 180. Consecutive Numbers


SELECT DISTINCT(L1.Num) AS ConsecutiveNums
FROM 
Logs L1,
Logs L2,
Logs L3
WHERE
L1.Id = L2.Id + 1
and L2.Id = L3.Id + 1
and L1.Num = L2.Num
and L2.Num = L3.Num

