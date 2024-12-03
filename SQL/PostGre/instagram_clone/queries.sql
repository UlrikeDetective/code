Select * from users;

SELECT id, username 
FROM users
WHERE username ILIKE '%Leipzig%';

SELECT id, username 
FROM users
WHERE username ILIKE '%Berlin%';

Select * from posts;

SELECT id, username, bio
FROM users
WHERE bio ILIKE '%travel%';

