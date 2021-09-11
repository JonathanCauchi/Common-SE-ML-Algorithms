-- 185. Department Top Three Salaries

with CTE as
(SELECT D.Name as Department, E.Name as Employee, E.Salary AS Salary, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS ranking
 FROM Employee as E
 LEFT JOIN Department as D
 ON E.DepartmentID = D.Id
)
SELECT Department, Employee, Salary
FROM CTE
WHERE ranking <= 3

-- 262. Trips and Users

with CTE as
(
SELECT T.Request_at as 'Day', ROUND(SUM(CASE WHEN T.Status LIKE 'cancelled%' THEN 1 ELSE 0 END)/COUNT(*),2) AS 'Cancellation Rate'
    FROM Trips as T
    INNER JOIN Users as U
    ON
    (
        (T.Client_Id = U.Users_ID) -- OR (T.Driver_Id = U.Users_ID)
    )
    WHERE U.Banned = 'No'
    AND T.Request_at between '2013-10-01' and '2013-10-03'
    GROUP BY Day
) 
SELECT *
FROM CTE

