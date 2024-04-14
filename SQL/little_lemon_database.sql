create Database little_lemon;

use little_lemon;

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
