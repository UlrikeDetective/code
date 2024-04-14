Use little_lemon;

## There are two main objectives of this activity:   
# * Create an INNER JOIN query. 
# * Create a Left JOIN query.  
 
## Task Instructions 
# Please attempt the following tasks: 
 
# **Task 1:** Little Lemon want a list of all customers who have made bookings. Write an INNER JOIN SQL statement to combine the full name and the phone number of each customer from the Customers table with the related booking date and 'number of guests' from the Bookings table. The expected output result should be the same as the following screenshot (assuming that you have created and populate the tables correctly.) 


SELECT Customers.FullName, Customers.PhoneNumber, Bookings.BookingDate, Bookings.NumberOfGuests 
FROM Customers INNER JOIN Bookings 
ON Customers.CustomerID = Bookings.CustomerID;

# **Task 2:** Little Lemon want to view information about all existing customers with bookings that have been made so far. This data must include customers who haven’t made any booking yet. Write a LEFT JOIN SQL statement to view the customer id from Customers table and the related booking id from the Bookings table. The expected output result should be the same as the following screenshot (assuming that you have created and populate the tables correctly.)


SELECT Customers.CustomerID, Bookings.BookingID 
FROM Customers LEFT JOIN Bookings 
ON Customers.CustomerID = Bookings.CustomerID;

SELECT Customers.FullName, Customers.PhoneNumber, Bookings.BookingDate, Bookings.NumberOfGuests 
FROM Customers INNER JOIN Bookings 
ON Customers.CustomerID = Bookings.CustomerID
where Customers.FullName = 'Rachel Green';

  
-- **Task 2:** Write a SQL SELECT query to find the menu items that are more expensive than all the 'Starters' and 'Desserts' menu item types. 
SELECT * FROM MenuItems WHERE Price > ALL (SELECT Price FROM MenuItems WHERE Type IN ('Starters', 'Desserts')); 
-- **Task 3:**  Write a SQL SELECT query to find the menu items that costs the same as the starter menu items that are Italian cuisine. 
SELECT *
FROM MenuItems
WHERE
    Price = (SELECT 
            Price
        FROM
            Menus,
            MenuItems
        WHERE
            Menus.ItemID = MenuItems.ItemID
                AND MenuItems.Type = 'Starters'
                AND Cuisine = 'Italian'); 
-- **Task 4:** Write a SQL SELECT query to find the menu items that were not ordered by the guests who placed bookings. 
SELECT *
FROM MenuItems
WHERE
    NOT EXISTS( SELECT 
            *
        FROM
            TableOrders,
            Menus
        WHERE
            TableOrders.MenuID = Menus.MenuID
                AND Menus.ItemID = MenuItems.ItemID); 

SELECT *
FROM MenuItems
WHERE EXISTS (
    SELECT *
    FROM TableOrders
    JOIN Menus ON TableOrders.MenuID = Menus.MenuID
    WHERE Menus.ItemID = MenuItems.ItemID
);

-- Task 1 solution: Find the minimum and the maximum average prices at which the customers can purchase food and drinks. 
-- The following query returns the average prices of menu items by their type:

SELECT Type, ROUND(AVG(Price), 2) AS avgPrice
FROM MenuItems
GROUP BY Type;


-- It can, in turn, be the source from which data (average price) is used to find the min and max average prices. 
-- So, you write this outer SELECT statement and add the above query as a subquery in its FROM clause as follows:

SELECT ROUND(MIN(avgPrice),2), ROUND(MAX(avgPrice),2) 
FROM (SELECT Type,AVG(Price) AS avgPrice
FROM MenuItems 
GROUP BY Type) AS aPrice;

-- The highlighted subquery in the FROM clause behaves as a temporary table in this case,
--  and it becomes the source or target table for the outer query.

-- Task 2 solution: Insert data of menu items with a minimum price based on the 'Type' into the LowCostMenuItems table. 
-- Here, the SELECT statement in INSERT INTO, contains the subquery.

INSERT INTO LowCostMenuItems 
SELECT ItemID,Name,Price 
FROM MenuItems 
WHERE Price =ANY(SELECT MIN(Price) FROM MenuItems GROUP BY Type);

Select * From LowCostMenuItems;

-- Task 3 solution: Delete all the low-cost menu items whose price is more than the minimum price of menu items that have a price between $5 and $10. 

 
DELETE FROM LowCostMenuItems 
WHERE Price > ALL(SELECT MIN(Price) as p 
FROM MenuItems 
GROUP BY Type 
HAVING p BETWEEN 5 AND 10);

select * from LowCostMenuItems;


Select * From HighCostMenuItems;

SELECT BookingDate, COUNT(BookingDate) 
FROM Bookings 
GROUP BY BookingDate;

REPLACE INTO Courses (CourseName, Cost) VALUES ("Kabasa", 20.00);

-- The outer SELECT query uses the ANY operator to find ANY matches from the values returned from the subquery – 
-- which gives a list of minimum prices of menu items based on their types. If it finds any matches, 
-- it will insert them into the LowCostMenuItems table.

SELECT FullName 
FROM Customers 
WHERE (SELECT CustomerID FROM Bookings WHERE Customers.CustomerID = Bookings.CustomerID and BookingDate = "2021-11-11");

-- Select all data from the BookingsView virtual table. The expected output result should be the same as shown in the following screenshot.
CREATE VIEW BookingsView AS SELECT BookingID, BookingDate, NumberOfGuests FROM Bookings 
WHERE NumberOfGuests > 3 AND BookingDate < "2021-11-13";

select * from BookingsView;

SELECT 
    CONCAT('ID: ',
            BookingID,
            ', Date: ',
            BookingDate,
            ', Number of guests: ',
            NumberOfGuests) AS 'Booking Details'
FROM
    Bookings;

SELECT 
    Customers.FullName, Bookings.BookingID
FROM
    Customers
        LEFT JOIN
    Bookings ON Customers.CustomerID = Bookings.CustomerID;



