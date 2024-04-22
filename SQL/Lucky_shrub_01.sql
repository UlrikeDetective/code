use Lucky_shrub;
show tables;
select * from Addresses;
select * from Clients;
select * from Employees;
select * from Orders;
select * from Orders_02;
select * from Products;

Drop table Orders_new;
Drop table Employees;

CREATE TABLE Orders_02 (
    OrderID INT NOT NULL PRIMARY KEY,
    ClientID VARCHAR(10),
    ProductID VARCHAR(10),
    Quantity INT,
    Cost DECIMAL(6 , 2 ),
    Date DATE
); 

INSERT INTO Orders_02(OrderID, ClientID, ProductID , Quantity, Cost, Date) VALUES
(1, "Cl1", "P1", 10, 500, "2020-09-01"),  
(2, "Cl2", "P2", 5, 100, "2020-09-05"),  
(3, "Cl3", "P3", 20, 800, "2020-09-03"),  
(4, "Cl4", "P4", 15, 150, "2020-09-07"),  
(5, "Cl3", "P3", 10, 450, "2020-09-08"),  
(6, "Cl2", "P2", 5, 800, "2020-09-09"),  
(7, "Cl1", "P4", 22, 1200, "2020-09-10"),  
(8, "Cl3", "P1", 15, 150, "2020-09-10"),  
(9, "Cl1", "P1", 10, 500, "2020-09-12"),  
(10, "Cl2", "P2", 5, 100, "2020-09-13"),  
(11, "Cl4", "P5", 5, 100, "2020-09-15"), 
(12, "Cl1", "P1", 10, 500, "2022-09-01"),  
(13, "Cl2", "P2", 5, 100, "2022-09-05"),  
(14, "Cl3", "P3", 20, 800, "2022-09-03"),  
(15, "Cl4", "P4", 15, 150, "2022-09-07"),  
(16, "Cl3", "P3", 10, 450, "2022-09-08"),  
(17, "Cl2", "P2", 5, 800, "2022-09-09"),  
(18, "Cl1", "P4", 22, 1200, "2022-09-10"),  
(19, "Cl3", "P1", 15, 150, "2022-09-10"),  
(20, "Cl1", "P1", 10, 500, "2022-09-12"),  
(21, "Cl2", "P2", 5, 100, "2022-09-13"),   
(22, "Cl2", "P1", 10, 500, "2021-09-01"),  
(23, "Cl2", "P2", 5, 100, "2021-09-05"),  
(24, "Cl3", "P3", 20, 800, "2021-09-03"),  
(25, "Cl4", "P4", 15, 150, "2021-09-07"),  
(26, "Cl1", "P3", 10, 450, "2021-09-08"),  
(27, "Cl2", "P1", 20, 1000, "2022-09-01"),  
(28, "Cl2", "P2", 10, 200, "2022-09-05"),  
(29, "Cl3", "P3", 20, 800, "2021-09-03"),  
(30, "Cl1", "P1", 10, 500, "2022-09-01"); 

CREATE TABLE Orders (
    OrderID INT,
    Department VARCHAR(100),
    OrderDate DATE,
    OrderQty INT,
    OrderTotal INT,
    PRIMARY KEY (OrderID)
); 

INSERT INTO Orders 
VALUES(1,'Lawn Care','2022-05-05',12,500),
(2,'Decking','2022-05-22',150,1450),
(3,'Compost and Stones','2022-05-27',20,780),
(4,'Trees and Shrubs','2022-06-01',15,400),
(5,'Garden Decor','2022-06-10',2,1250),
(6,'Lawn Care','2022-06-10',12,500),
(7,'Decking','2022-06-25',150,1450),
(8,'Compost and Stones','2022-05-29',20,780),
(9,'Trees and Shrubs','2022-06-10',15,400),
(10,'Garden Decor','2022-06-10',2,1250),
(11,'Lawn Care','2022-06-25',10,400), 
(12,'Decking','2022-06-25',100,1400),
(13,'Compost and Stones','2022-05-30',15,700),
(14,'Trees and Shrubs','2022-06-15',10,300),
(15,'Garden Decor','2022-06-11',2,1250),
(16,'Lawn Care','2022-06-10',12,500),
(17,'Decking','2022-06-25',150,1450),
(18,'Trees and Shrubs','2022-06-10',15,400),
(19,'Lawn Care','2022-06-10',12,500),
(20,'Decking','2022-06-25',150,1450),
(21,'Decking','2022-06-25',150,1450);

INSERT INTO Orders VALUES
(31,'Lawn Care','2022-07-05',24,1000),
(32,'Decking','2022-07-22',300,2900),
(33,'Compost and Stones','2022-07-27',40,1500),
(34,'Trees and Shrubs','2022-07-01',45,1000),
(35,'Garden Decor','2022-07-10',4,2500),
(36,'Lawn Care','2022-07-10',25,1100),
(37,'Decking','2022-07-25',50,450),
(38,'Compost and Stones','2022-07-29',10,500),
(39,'Trees and Shrubs','2022-07-10',50,1400),
(40,'Garden Decor','2022-07-10',20,12000),
(41,'Lawn Care','2022-07-25',10,400), 
(42,'Decking','2022-07-25',100,1400),
(43,'Compost and Stones','2022-07-30',15,700),
(44,'Trees and Shrubs','2022-07-15',10,300),
(45,'Garden Decor','2022-07-11',2,1250),
(46,'Lawn Care','2022-07-10',2,100),
(47,'Decking','2022-07-25',100,1000),
(48,'Trees and Shrubs','2022-07-10',15,400),
(49,'Lawn Care','2022-07-10',20,900),
(50,'Trees and Shrubs','2022-07-25',100,1000),
(51,'Decking','2022-07-25',150,1450);

CREATE TABLE employees (
  EmployeeID int NOT NULL,
  EmployeeName varchar(150) DEFAULT NULL,
  Department varchar(150) DEFAULT NULL,
  ContactNo varchar(12) DEFAULT NULL,
  Email varchar(100) DEFAULT NULL,
  AnnualSalary int DEFAULT NULL,
  PRIMARY KEY (EmployeeID)
);

INSERT INTO employees VALUES 
(1,'Seamus Hogan', 'Recruitment', '351478025', 'Seamus.h@luckyshrub.com',50000), 
(2,'Thomas Eriksson', 'Legal', '351475058', 'Thomas.e@luckyshrub.com',75000), 
(3,'Simon Tolo', 'Marketing', '351930582','Simon.t@luckyshrub.com',40000), 
(4,'Francesca Soffia', 'Finance', '351258569','Francesca.s@luckyshrub.com',45000), 
(5,'Emily Sierra', 'Customer Service', '351083098','Emily.s@luckyshrub.com',35000), 
(6,'Maria Carter', 'Human Resources', '351022508','Maria.c@luckyshrub.com',55000),
(7,'Rick Griffin', 'Marketing', '351478458','Rick.G@luckyshrub.com',50000);

INSERT INTO employees (EmployeeID, EmployeeName, Department, ContactNo, Email, AnnualSalary)
VALUES 
(8, 'Lily Evans', 'Human Resources', '555123456', 'lily.evans@example.com', 55000),
(9, 'James Potter', 'Sales', '555234567', 'james.potter@example.com', 60000),
(10, 'Sirius Black', 'Marketing', '555345678', 'sirius.black@example.com', 52000),
(11, 'Remus Lupin', 'Finance', '555456789', 'remus.lupin@example.com', 58000),
(12, 'Peter Pettigrew', 'Operations', '555567890', 'peter.pettigrew@example.com', 51000),
(13, 'Nymphadora Tonks', 'Customer Service', '555678901', 'nymphadora.tonks@example.com', 53000),
(14, 'Arthur Weasley', 'IT', '555789012', 'arthur.weasley@example.com', 57000),
(15, 'Molly Weasley', 'Administration', '555890123', 'molly.weasley@example.com', 54000),
(16, 'Albus Dumbledore', 'Management', '555901234', 'albus.dumbledore@example.com', 65000),
(17, 'Minerva McGonagall', 'Education', '555012345', 'minerva.mcgonagall@example.com', 62000);

INSERT INTO employees (EmployeeID, EmployeeName, Department, ContactNo, Email, AnnualSalary)
VALUES 
(18, 'Katniss Everdeen', 'Archery Division', '555111111', 'katniss.everdeen@example.com', 60000),
(19, 'Peeta Mellark', 'Bakery Department', '555222222', 'peeta.mellark@example.com', 55000),
(20, 'Gale Hawthorne', 'Forestry Division', '555333333', 'gale.hawthorne@example.com', 52000),
(21, 'Haymitch Abernathy', 'Mentoring Department', '555444444', 'haymitch.abernathy@example.com', 58000),
(22, 'Effie Trinket', 'Event Planning', '555555555', 'effie.trinket@example.com', 54000),
(23, 'Primrose Everdeen', 'Medical Division', '555666666', 'primrose.everdeen@example.com', 53000),
(24, 'Finnick Odair', 'Fishing Department', '555777777', 'finnick.odair@example.com', 59000),
(25, 'Johanna Mason', 'Combat Training', '555888888', 'johanna.mason@example.com', 57000),
(26, 'Rue Everdeen', 'Botanical Garden', '555999999', 'rue.everdeen@example.com', 51000),
(27, 'Cinna', 'Fashion Design', '555000000', 'cinna@example.com', 62000);

INSERT INTO employees (EmployeeID, EmployeeName, Department, ContactNo, Email, AnnualSalary)
VALUES 
(28, 'Rome Italy', 'Human Resources', '534523456', 'rome.italy@example.com', 58000),
(29, 'Madrid Spain', 'Sales', '445234567', 'madrid.spain@example.com', 54000),
(30, 'Lisbon Portugal', 'Marketing', '555345328', 'lisbon.portugalk@example.com', 62000),
(31, 'Dublin Ireland', 'Finance', '555455789', 'dublin.ireland@example.com', 88000),
(32, 'Stockholm Sweden', 'Operations', '559067890', 'stockholm.sweden@example.com', 65000),
(33, 'Oslo Norway', 'Customer Service', '599678901', 'oslo.norway@example.com', 58000),
(34, 'Berlin Germany', 'IT', '555789992', 'berlin.germany@example.com', 52000),
(35, 'Mexico City', 'Administration', '555510123', 'mexico.city@example.com', 64000),
(36, 'Delhi India', 'Management', '555988234', 'delhi.india@example.com', 69000),
(37, 'Male Maldives', 'Education', '555012345', 'male.maldives@example.com', 52000);

CREATE TABLE employee_orders (
 OrderID int NOT NULL,
 EmployeeID int NOT NULL,
 Status VARCHAR(150),
 HandlingCost int DEFAULT NULL,
 PRIMARY KEY (EmployeeID,OrderID),
 FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID),
 FOREIGN KEY (OrderID) REFERENCES orders(OrderID)
);

CREATE TABLE Notifications (
    NotificationID INT AUTO_INCREMENT,
    Notification VARCHAR(255),
    DateTime TIMESTAMP NOT NULL,
    PRIMARY KEY (NotificationID)
); 