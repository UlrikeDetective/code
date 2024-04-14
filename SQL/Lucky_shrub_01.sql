use Lucky_shrub;
show tables;
select * from Addresses;
select * from Clients;
select * from Employees;
select * from Orders;
select * from Products;

Drop table Orders;
Drop table Employees;

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


