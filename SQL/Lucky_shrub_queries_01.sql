Use lucky_shrub;

SELECT *
FROM orders
INNER JOIN products ON orders.ProductID = products.ProductID;

SELECT products.ProductName, COUNT(*) AS OrderCount
FROM orders
INNER JOIN products ON orders.ProductID = products.ProductID
GROUP BY products.ProductName;

## Exercise Instructions
# Please attempt the following tasks.
 
-- **Task 1:** Write a SQL SELECT statement to group all records that have the same order date.   
-- The expected output result should be the same as the following screenshot 
-- (assuming that you have created and populated the tables correctly.) 

SELECT OrderDate FROM Orders GROUP BY OrderDate;

-- **Task 2:** Write a SQL SELECT statement to retrieve the number of orders placed on the same day.
-- The expected output result should be the same as the following screenshot 
-- (assuming that you have created and populated the tables correctly.) 

SELECT OrderDate,COUNT(OrderID) FROM Orders GROUP BY OrderDate;
 
-- **Task 3:** Write a SQL SELECT statement to retrieve the total order quantities placed by each department.
-- The expected output result should be the same as the following screenshot (assuming that you have created and 
-- populated the tables correctly.) 

SELECT Department, SUM(OrderQty) FROM Orders GROUP BY Department;
 
-- **Task 4 :** Write a SQL SELECT statement to retrieve the number of orders placed on the same day between the following 
-- dates: 1st June 2022 and 30th June 2022. 
-- The expected output result should be the same as the following screenshot (assuming that you have created and populated 
-- the tables correctly.) 

SELECT OrderDate,COUNT(OrderID) FROM Orders GROUP BY OrderDate HAVING OrderDate BETWEEN '2022-06-01' AND '2022-06-30';

-- Tasks
-- Task1: Use the ANY operator to identify all employees with the Order Status status 'Completed'. 
-- Task 2: Use the ALL operator to identify the IDs of employees who earned a handling cost of "more than 20% of the order value" 
-- from all orders they have handled.
-- Task 3: Use the GROUP BY clause to summarize the duplicate records with the same column values into a single record
--  by grouping them based on those columns.
-- Task 4: Use the HAVING clause to filter the grouped data in the subquery that you wrote in 
-- task 3 to filter the 20% OrderTotal values to only retrieve values that are more than $100.


-- Task 1 solution: Use the ANY operator to identify all employees with the Order Status status 'Completed'. 
SELECT EmployeeId, EmployeeName  
FROM employees  
WHERE EmployeeID = ANY (SELECT EmployeeID FROM employee_orders WHERE Status='Completed'); 

SELECT EmployeeID,HandlingCost 
FROM employee_orders  
WHERE HandlingCost > ALL(SELECT ROUND(OrderTotal/100 * 20) FROM orders); 