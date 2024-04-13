use Lucky_shrub;
show tables;
select * from Addresses;
select * from Clients;
select * from Employees;
select * from Orders;
select * from Products;

SELECT *
FROM orders
INNER JOIN products ON orders.ProductID = products.ProductID;

SELECT products.ProductName, COUNT(*) AS OrderCount
FROM orders
INNER JOIN products ON orders.ProductID = products.ProductID
GROUP BY products.ProductName;
