create Database little_lemon;

use little_lemon;

select * from customers;

drop table Customers;

CREATE TABLE Customers(  
CustomerID INT NOT NULL PRIMARY KEY,   
FullName VARCHAR(100) NOT NULL,    
PhoneNumber INT NOT NULL UNIQUE  
); 

INSERT INTO Customers( CustomerID, FullName, PhoneNumber) 
VALUES (1, "Vanessa McCarthy", 0757536378), 
(2, "Marcos Romero", 0757536379), 
(3, "Hiroki Yamane", 0757536376), 
(4, "Anna Iversen", 0757536375), 
(5, "Diana Pinto", 0757536374),
(6, "Lemon Lemonade", 0757526284),
(7, "Simon Law", 0757596784),
(8, "Rubert Solo", 0755426784)
; 

INSERT INTO little_lemon.Customers (CustomerID, FullName, PhoneNumber)
VALUES 
(9, 'Vanessa McCarthy', '0757736378'),
(10, 'Liam Johnson', '0712345578'),
(11, 'Sophia Williams', '0713456789'),
(12, 'Noah Brown', '0744567890'),
(13, 'Emma Jones', '0725678901'),
(14, 'Oliver Davis', '0755789012'),
(15, 'Ava Wilson', '0767892123'),
(16, 'William Taylor', '0778907234'),
(17, 'Isabella Martinez', '0769012345'),
(18, 'James Anderson', '0790523456');

INSERT INTO little_lemon.Customers (CustomerID, FullName, PhoneNumber)
VALUES 
(19, 'Rachel Green', '0447536378'),
(20, 'Ross Geller', '0755345678'),
(21, 'Monica Geller', '0663456789'),
(22, 'Chandler Bing', '0737767890'),
(23, 'Joey Tribbiani', '0748878901'),
(24, 'Phoebe Buffay', '0759989012'),
(25, 'Gunther Central Perk', '0700890123'),
(26, 'Janice Hosenstein', '0711901234'),
(27, 'Richard Burke', '0782212345'),
(28, 'Carol Willick-Bunch', '0794423456');

INSERT INTO little_lemon.Customers (CustomerID, FullName, PhoneNumber)
VALUES 
(29, 'Marie Curie', '0447536319'),
(30, 'Malala Yousafzai', '0447536318'),
(31, 'Dorothy Crowfoot Hodgkin', '0447536317'),
(32, 'Mother Teresa', '0447536316'),
(33, 'Rosalind Franklin', '0447536315'),
(34, 'Wangari Maathai', '0447536314'),
(35, 'Shirin Ebadi', '0447536313'),
(36, 'Ada Yonath', '0447536312'),
(37, 'Tu Youyou', '0447536311'),
(38, 'Aung San Suu Kyi', '0447536310');


CREATE TABLE Bookings (  
BookingID INT NOT NULL PRIMARY KEY,  
BookingDate DATE NOT NULL,  
TableNumber INT NOT NULL,   
NumberOfGuests INT NOT NULL CHECK ( NumberOfGuests <= 8),  
CustomerID INT NOT NULL,  
FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE ON UPDATE CASCADE   
); 

INSERT INTO Bookings ( BookingID, BookingDate, TableNumber, NumberOfGuests, CustomerID) 
VALUES (10, '2021-11-11', 7, 5, 1), (11, '2021-11-10', 5, 2, 2), (12, '2021-11-10', 3, 2, 4),
(13, '2021-12-11', 7, 3, 6), (14, '2021-12-10', 5, 5, 7), (15, '2021-12-10', 3, 6, 8),
(16, '2021-12-14', 2, 8, 3), (17, '2021-12-14', 6, 2, 7), (18, '2021-12-14', 5, 8, 6),
(19, '2021-12-21', 7, 7, 6), (20, '2021-12-19', 5, 4, 7), (21, '2021-12-17', 3, 8, 8)
;   

INSERT INTO Bookings (BookingID, BookingDate, TableNumber, NumberOfGuests, CustomerID) 
VALUES 
(22, '2022-01-02', 1, 5, 11),
(23, '2022-01-03', 2, 3, 22),
(24, '2022-01-04', 3, 4, 13),
(25, '2022-01-05', 4, 6, 24),
(26, '2022-01-06', 5, 7, 25),
(27, '2022-01-07', 6, 2, 36),
(28, '2022-01-08', 7, 8, 37),
(29, '2022-01-09', 8, 5, 38),
(30, '2022-01-10', 1, 3, 29),
(31, '2022-01-11', 2, 4, 10),
(32, '2022-01-12', 3, 5, 11),
(33, '2022-01-13', 4, 6, 12),
(34, '2022-01-14', 5, 7, 13),
(35, '2022-01-15', 6, 3, 14),
(36, '2022-01-16', 7, 4, 15),
(37, '2022-01-17', 8, 5, 16),
(38, '2022-01-18', 1, 6, 17),
(39, '2022-01-19', 2, 7, 18),
(40, '2022-01-20', 3, 2, 19),
(41, '2022-01-21', 4, 3, 20),
(42, '2022-01-22', 5, 4, 21),
(43, '2022-01-23', 6, 5, 22),
(44, '2022-01-24', 7, 6, 23),
(45, '2022-01-25', 8, 7, 24),
(46, '2022-01-26', 1, 2, 25),
(47, '2022-01-27', 2, 3, 26),
(48, '2022-01-28', 3, 4, 27),
(49, '2022-01-29', 4, 5, 28),
(50, '2022-01-30', 5, 6, 29),
(51, '2022-01-31', 6, 7, 30),
(52, '2022-01-02', 7, 8, 31),
(53, '2022-01-03', 8, 5, 32),
(54, '2022-01-04', 1, 3, 33),
(55, '2022-01-05', 2, 4, 34),
(56, '2022-01-06', 3, 5, 35),
(57, '2022-01-07', 4, 6, 36),
(58, '2022-01-08', 5, 7, 37),
(59, '2022-01-09', 6, 2, 38),
(60, '2022-01-10', 7, 3, 1),
(61, '2022-01-11', 8, 4, 2),
(62, '2022-01-12', 1, 5, 3),
(63, '2022-01-13', 2, 6, 4),
(64, '2022-01-14', 3, 7, 5),
(65, '2022-01-15', 4, 3, 6),
(66, '2022-01-16', 5, 4, 7),
(67, '2022-01-17', 6, 5, 8),
(68, '2022-01-18', 7, 6, 9),
(69, '2022-01-19', 8, 7, 10),
(70, '2022-01-20', 1, 2, 11),
(71, '2022-01-21', 2, 3, 12),
(72, '2022-01-22', 3, 4, 13),
(73, '2022-01-23', 4, 5, 14),
(74, '2022-01-24', 5, 6, 15);

CREATE TABLE MenuItems ( 
  ItemID INT, 
  Name VARCHAR(200), 
  Type VARCHAR(100), 
  Price INT, 
  PRIMARY KEY (ItemID) 
);  

INSERT INTO MenuItems 
VALUES(1,'Olives','Starters',5), 
(2,'Flatbread','Starters', 5), 
(3, 'Minestrone', 'Starters', 8), 
(4, 'Tomato bread','Starters', 8), 
(5, 'Falafel', 'Starters', 7), 
(6, 'Hummus', 'Starters', 5), 
(7, 'Greek salad', 'Main Courses', 15), 
(8, 'Bean soup', 'Main Courses', 12), 
(9, 'Pizza', 'Main Courses', 15), 
(10,'Greek yoghurt','Desserts', 7), 
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4), 
(13, 'Athens White wine', 'Drinks', 25), 
(14, 'Corfu Red Wine', 'Drinks', 30), 
(15, 'Turkish Coffee', 'Drinks', 10), 
(16, 'Turkish Coffee', 'Drinks', 10), 
(17, 'Kabasa', 'Main Courses', 17); 

INSERT INTO MenuItems (ItemID, Name, Type, Price) 
VALUES 
(18, 'Lamb Souvlaki', 'Main Courses', 20),
(19, 'Moussaka', 'Main Courses', 18),
(20, 'Baklava', 'Desserts', 8),
(21, 'Tiramisu', 'Desserts', 9),
(22, 'Baklava Ice Cream', 'Desserts', 10),
(23, 'Ouzo', 'Drinks', 12),
(24, 'Retsina', 'Drinks', 14);


CREATE TABLE Menus ( 
  MenuID INT, 
  ItemID INT, 
  Cuisine VARCHAR(100), 
  PRIMARY KEY (MenuID,ItemID) 
); 

INSERT INTO Menus (MenuID, ItemID, Cuisine)
SELECT 1, ItemID, 'Greek' FROM MenuItems WHERE ItemID IN (1, 7, 10, 13, 18)
UNION ALL
SELECT 2, ItemID, 'Italian' FROM MenuItems WHERE ItemID IN (3, 9, 12, 15, 19)
UNION ALL
SELECT 3, ItemID, 'Turkish' FROM MenuItems WHERE ItemID IN (5, 17, 11, 16, 20, 21, 22, 23, 24);

drop table TableOrders;

CREATE TABLE TableOrders ( 
  OrderID INT, 
  TableNo INT, 
  MenuID INT, 
  BookingID INT, 
  BillAmount INT, 
  Quantity INT, 
  PRIMARY KEY (OrderID,TableNo));
  
INSERT INTO TableOrders (OrderID, TableNo, MenuID, BookingID, BillAmount, Quantity)
SELECT
    ROW_NUMBER() OVER (ORDER BY B.BookingID) AS OrderID,  -- Generate unique OrderID values
    B.TableNumber AS TableNo,
    M.ItemID AS MenuID,
    B.BookingID,
    (MI.Price * B.NumberOfGuests) AS BillAmount,
    B.NumberOfGuests AS Quantity
FROM
    Bookings B
JOIN
    Menus M ON B.TableNumber = M.MenuID
JOIN
    MenuItems MI ON M.ItemID = MI.ItemID;

Select * From TableOrders;

-- Create the LowCostMenuItems table
CREATE TABLE LowCostMenuItems (
    ItemID INT,
    Name VARCHAR(200),
    Price INT
);

-- Insert into LowCostMenuItems
INSERT INTO LowCostMenuItems
SELECT ItemID, Name, Price
FROM MenuItems
WHERE Price = ANY (
    SELECT MIN(Price)
    FROM MenuItems
    GROUP BY Type
);

-- Create the HighCostMenuItems table
CREATE TABLE HighCostMenuItems (
    ItemID INT,
    Name VARCHAR(200),
    Price INT
);

INSERT INTO HighCostMenuItems
SELECT ItemID, Name, Price
FROM MenuItems
WHERE Price = ANY (
    SELECT Max(Price)
    FROM MenuItems
    GROUP BY Type
);

CREATE TABLE Courses (
    CourseName VARCHAR(255) PRIMARY KEY,
    Cost DECIMAL(4 , 2 )
); 

Insert into Courses (CourseName, Cost) 
VALUES 
("Greek salad", 15.50), 
("Bean soup", 12.25),
 ("Pizza", 15.00),
 ("Carbonara", 12.50),
 ("Kabasa", 17.00), 
 ("Shwarma", 11.30); 

CREATE TABLE DeliveryAddress(     
    ID INT PRIMARY KEY,     
    Address VARCHAR(255) NOT NULL,     
    Type VARCHAR(100) NOT NULL DEFAULT "Private",     
    CustomerID INT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID));
    
ALTER TABLE Courses ADD COLUMN Ingredients VARCHAR(255); 
 