SELECT MAX(id) FROM followers;

Select * from followers limit 10;
TRUNCATE TABLE followers RESTART IDENTITY;

-- Insert sample followers
INSERT INTO followers (follower_id, following_id) VALUES
(1, 2), (2, 1), (1, 3), (3, 1),(4, 2), 
(3, 2), (3, 4), (3, 6), (3, 8), (3, 10);

-- instert random followers
-- 1. Create Influencers (Large Gap)
-- Every user follows up to 15 people from a random "Elite" pool of 20
INSERT INTO followers (follower_id, following_id)
WITH influencers AS (
    SELECT id FROM users ORDER BY random() LIMIT 20
)
SELECT u.id, i.id
FROM users u
CROSS JOIN LATERAL (
    SELECT id FROM influencers 
    WHERE id != u.id 
    ORDER BY random() 
    LIMIT floor(random() * 15)
) i
ON CONFLICT DO NOTHING;

-- 2. Create Regular "Social" follows
-- Everyone follows 3 completely random people
INSERT INTO followers (follower_id, following_id)
SELECT u.id, r.id
FROM users u
CROSS JOIN LATERAL (
    SELECT id FROM users 
    WHERE id != u.id 
    ORDER BY random() 
    LIMIT 3
) r
ON CONFLICT DO NOTHING;

-- 3. The Follow-Back (The Mutual Effect)
-- Select existing follows and flip them (with a 40% probability)
INSERT INTO followers (follower_id, following_id)
SELECT following_id, follower_id
FROM followers
WHERE random() < 0.40
ON CONFLICT DO NOTHING;

select * from followers;

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
WHERE f.follower_id = 100;

-- Add a new follower:
INSERT INTO followers (follower_id, following_id)
VALUES (2, 11), (11, 4), (11, 6);

-- remove a follower
DELETE FROM followers
WHERE follower_id = 2 AND following_id = 3;

