Use join_us;

CREATE TABLE users (
    email VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW()
);

describe users;

INSERT INTO users (email) VALUES('Katie34@yahoo.com'), ('Tunde@gmail.com');

Select * From users;

SELECT 
    DATE_FORMAT(Max(created_at), "%M %D %Y") as earliest_date 
FROM users;

SELECT * 
FROM   users 
WHERE  created_at = (SELECT Max(created_at) 
                     FROM   users); 
                     
SELECT Monthname(created_at) AS month, 
       Count(*)              AS count 
FROM   users 
GROUP  BY month 
ORDER  BY count DESC; 

SELECT Count(*) AS yahoo_users 
FROM   users 
WHERE  email LIKE '%@yahoo.com'; 

SELECT CASE 
         WHEN email LIKE '%@gmail.com' THEN 'gmail' 
         WHEN email LIKE '%@yahoo.com' THEN 'yahoo' 
         WHEN email LIKE '%@hotmail.com' THEN 'hotmail' 
         ELSE 'other' 
       end      AS provider, 
       Count(*) AS total_users 
FROM   users 
GROUP  BY provider 
ORDER  BY total_users DESC; 