-- 179. Reformat Department Table

SELECT DISTINCT(id),
MAX(CASE WHEN month = 'Jan' THEN revenue else NULL END) Jan_Revenue,

MAX(CASE WHEN month = 'Feb' THEN revenue else NULL END) Feb_Revenue,

MAX(CASE WHEN month = 'Mar' THEN revenue else NULL END) Mar_Revenue,

MAX(CASE WHEN month = 'Apr' THEN revenue else NULL END) Apr_Revenue,

MAX(CASE WHEN month = 'May' THEN revenue else NULL END) May_Revenue,

MAX(CASE WHEN month = 'Jun' THEN revenue else NULL END) Jun_Revenue,

MAX(CASE WHEN month = 'Jul' THEN revenue else NULL END) Jul_Revenue,

MAX(CASE WHEN month = 'Aug' THEN revenue else NULL END) Aug_Revenue,

MAX(CASE WHEN month = 'Sep' THEN revenue else NULL END) Sep_Revenue,

MAX(CASE WHEN month = 'Oct' THEN revenue else NULL END) Oct_Revenue,

MAX(CASE WHEN month = 'Nov' THEN revenue else NULL END) Nov_Revenue,

MAX(CASE WHEN month = 'Dec' THEN revenue else NULL END) Dec_Revenue

FROM Department
ORDER BY id

-- 183. Customers Who Never Order

Select c.Name as Customers
FROM Customers as c
WHERE c.Id NOT IN
(
    SELECT c.Id
    FROM Customers as c, Orders as o
    WHERE c.Id = o.CustomerId
)


