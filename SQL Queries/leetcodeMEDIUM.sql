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
