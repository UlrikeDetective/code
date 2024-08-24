Use join_us;

drop table users2;

CREATE TABLE users2 (
    firstName VARCHAR(100),
    lastName VARCHAR(100),  -- corrected typo in field name
    sex VARCHAR(50),
    jobTitle VARCHAR(255),
    email VARCHAR(255) PRIMARY KEY,
    address VARCHAR(255),
    city VARCHAR(100),
    zipcode Varchar(20),
    country VARCHAR(100),
    latitude INT(100),
    longitude INT(100),
    amount DECIMAL(10, 2),
    company VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

describe users2;

select * from users2;

SELECT 
    DATE_FORMAT(MIN(created_at), "%M %D %Y") as earliest_date 
FROM users2;

SELECT firstName, lastName
FROM   users2 
WHERE  created_at = (SELECT Min(created_at) 
                     FROM   users2);
                     
SELECT Monthname(created_at) AS month, 
       Count(*)              AS count 
FROM   users2 
GROUP  BY month 
ORDER  BY count DESC; 

SELECT Count(*) AS yahoo_users 
FROM   users2 
WHERE  email LIKE '%@yahoo.com'; 

SELECT CASE 
         WHEN email LIKE '%@gmail.com' THEN 'gmail' 
         WHEN email LIKE '%@yahoo.com' THEN 'yahoo' 
         WHEN email LIKE '%@hotmail.com' THEN 'hotmail' 
         ELSE 'other' 
       end      AS provider, 
       Count(*) AS total_users 
FROM   users2 
GROUP  BY provider 
ORDER  BY total_users DESC; 

SELECT city, 
       Count(*)              AS count 
FROM   users2 
GROUP  BY city 
ORDER  BY count DESC; 

SELECT city, COUNT(*) AS count
FROM users2
WHERE country = 'Germany'
GROUP BY city
ORDER BY count DESC;

SELECT country, COUNT(*) AS count
FROM users2
WHERE country LIKE '%@United%'
GROUP BY country
ORDER BY count DESC;


SELECT country, 
       Count(*)              AS count 
FROM   users2 
GROUP  BY country 
ORDER  BY count DESC; 