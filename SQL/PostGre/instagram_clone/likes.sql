-- Insert sample likes
INSERT INTO likes (user_id, post_id) VALUES
(1, 2), (2, 1), (3, 1), (1, 3),(3, 2),
(4, 2), (4, 1), (4, 8), (4, 7),(4, 6),
(6, 5), (6, 6), (6, 7), (6, 8),(7, 2),
(8, 2), (8, 1), (9, 1), (10, 3),(9, 2);

-- List all likes on a specific post:
SELECT u.username
FROM likes l
JOIN users u ON l.user_id = u.id
WHERE l.post_id = 1;

-- Count likes on a specific post:
SELECT COUNT(*) AS like_count
FROM likes
WHERE post_id = 1;

SELECT COUNT(*) AS like_count
FROM likes
Order by post_id desc;

-- Add a like
INSERT INTO likes (user_id, post_id)
VALUES (11, 5);

-- remove a like
DELETE FROM likes
WHERE user_id = 3 AND post_id = 1;
