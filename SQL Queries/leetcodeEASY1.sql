-- 595. Big Countries

SELECT w.name, w.population, w.area
FROM World as w
WHERE w.area > 3000000 OR w.population > 25000000

-- 176. Second Highest Salary

SELECT Salary as SecondHighestSalary
FROM Employee AS e 
WHERE Salary = ( SELECT MAX(Salary) as Salary
          FROM Employee as e
          WHERE Salary < (SELECT MAX(Salary) FROM Employee))
          
--------------------------------------
      
SELECT Salary as SecondHighestSalary
FROM Employee
LIMIT 1 OFFSET 1 

--------------------------------------

SELECT (SELECT Salary
        FROM Employee
        LIMIT 1 OFFSET 1
) AS SecondHighestSalary

-- 596. Classes More Than 5 Students

SELECT class
FROM courses
HAVING COUNT(DISTINCT(student))  > 5

----------------------------------------

SELECT (SELECT class
        FROM courses
        HAVING COUNT(DISTINCT(student))>5
) AS class

-- 627. Swap Salary

UPDATE salary
SET
    sex = CASE sex 
    WHEN 'm' 
    THEN 'f' 
    ELSE 'm' 
    END
    
-- 620. Not Boring Movies

SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 = 1
AND description != 'boring'
ORDER BY rating DESC

-- 182. Duplicate Emails

SELECT Email
FROM Person
HAVING COUNT(DISTINCT(Email)) > 1

-- 175. Combine Two Tables

SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as p
LEFT JOIN Address as a
ON p.PersonId = a.PersonId

