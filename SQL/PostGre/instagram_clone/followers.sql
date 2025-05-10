SELECT MAX(id) FROM followers;

Select * from followers limit 10;

-- Insert sample followers
INSERT INTO followers (follower_id, following_id) VALUES
(1, 2), (2, 1), (1, 3), (3, 1),(4, 2), 
(3, 2), (3, 4), (3, 6), (3, 8), (3, 10),
(5, 1), (5, 2), (5, 6), (5, 9),
(2, 6), (2, 7), (2, 8), (2, 10),
(4, 1), (4, 5), (4, 7), (4, 9), (4, 10),
(1, 7), (1, 10),
(7, 2), (7, 4), (7, 8), (7, 9),
(10, 9), (9, 10), 
(8,1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (8, 10);

SELECT COUNT(follower_id) AS follower_count, following_id
FROM followers
GROUP BY following_id
ORDER BY follower_count DESC;

SELECT COUNT(following_id) AS following_count, follower_id
FROM followers
GROUP BY follower_id
ORDER BY following_count DESC;

Select count(follower_id) as follower
from followers;

-- List all followers of a user:
SELECT u.username AS follower
FROM followers f
JOIN users u ON f.follower_id = u.id
WHERE f.following_id = 1;

-- List all users a person follows:
SELECT u.username AS following
FROM followers f
JOIN users u ON f.following_id = u.id
WHERE f.follower_id = 1;

-- Add a new follower:
INSERT INTO followers (follower_id, following_id)
VALUES (2, 11), (11, 4), (11, 6);

-- remove a follower
DELETE FROM followers
WHERE follower_id = 2 AND following_id = 3;

