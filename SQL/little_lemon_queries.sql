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