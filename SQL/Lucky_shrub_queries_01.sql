Use lucky_shrub;

SELECT *
FROM orders_02
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

SELECT OrderDate FROM Orders_02 GROUP BY OrderDate;

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

SELECT * FROM employees WHERE AnnualSalary >= 50000 AND Department = 'Marketing';
SELECT * FROM employees WHERE NOT AnnualSalary > 50000;
SELECT * FROM employees WHERE AnnualSalary < 50000 AND Department IN('Marketing', 'Finance', 'Legal');
SELECT * FROM employees WHERE AnnualSalary > 50000 AND Department IN('Marketing', 'Finance', 'Legal');
SELECT * FROM employees WHERE AnnualSalary BETWEEN 10000 AND 50000; 
SELECT * FROM employees WHERE EmployeeName LIKE 'S___%';

SELECT OrderDate FROM Orders GROUP BY OrderDate;
SELECT OrderDate,COUNT(OrderID) FROM Orders GROUP BY OrderDate;
SELECT Department, SUM(OrderQty) FROM Orders GROUP BY Department;
SELECT OrderDate,COUNT(OrderID) FROM Orders GROUP BY OrderDate HAVING OrderDate BETWEEN '2022-07-01' AND '2022-07-30';

SELECT EmployeeId, EmployeeName  
FROM employees  
WHERE EmployeeID = ANY (SELECT EmployeeID FROM employee_orders WHERE Status='Completed'); 

CREATE FUNCTION FindCost(order_id INT) 
RETURNS DECIMAL (5,2) DETERMINISTIC 
RETURN (SELECT Cost FROM Orders_02 WHERE OrderID = order_id);

DELIMITER // 
CREATE Procedure GetDiscount(OrderIDInput INT) 
     BEGIN 
         DECLARE cost_after_discount DECIMAL(7,2); 
         DECLARE current_cost DECIMAL(7,2); 
         DECLARE order_quantity INT; 
         SELECT Quantity INTO order_quantity FROM Orders WHERE OrderID = OrderIDInput; 
         SELECT Cost INTO current_cost FROM Orders WHERE OrderID = OrderIDInput; 
        IF order_quantity >= 20 THEN
          SET cost_after_discount = current_cost - (current_cost * 0.2);              
        ELSEIF order_quantity >= 10 THEN
          SET cost_after_discount = current_cost - (current_cost * 0.1); 
        ELSE SET cost_after_discount = current_cost;
        END IF;
    SELECT cost_after_discount; 
END//
DELIMITER ; 


DELIMITER //
CREATE TRIGGER ProductSellPriceInsertCheck 
    AFTER INSERT  
    ON Products FOR EACH ROW  
    BEGIN
    IF NEW.SellPrice <= NEW.BuyPrice THEN
        INSERT INTO Notifications(Notification,DateTime) 
        VALUES(CONCAT('A SellPrice same or less than the BuyPrice was inserted for ProductID ', NEW.ProductID), NOW()); 
    END IF;
    END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER ProductSellPriceUpdateCheck 
    AFTER UPDATE  
    ON Products FOR EACH ROW  
    BEGIN
    IF NEW.SellPrice <= NEW.BuyPrice THEN
        INSERT INTO Notifications(Notification,DateTime) 
        VALUES(CONCAT(NEW.ProductID,' was updated with a SellPrice of ', NEW.SellPrice,' which is the same or less than the BuyPrice'), NOW()); 
    END IF;
    END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER NotifyProductDelete 
    AFTER DELETE   
    ON Products FOR EACH ROW   
    INSERT INTO Notifications(Notification, DateTime) 
    VALUES(CONCAT('The product with a ProductID ', OLD.ProductID,' was deleted'), NOW()); 
END //
DELIMITER ;

SELECT OrderID, ProductID, Quantity, Date 
FROM Orders_02;

Explain SELECT OrderID, ProductID, Quantity, Date 
FROM Orders_02;

SELECT * FROM Orders_02 WHERE ClientID ='Cl1'; 

CREATE INDEX IdxClientID ON Orders_02(ClientID);
EXPLAIN SELECT * 
FROM Orders_02;

SELECT * FROM employees WHERE employeeName LIKE '%Tolo' WHERE ClientID='Cl1';