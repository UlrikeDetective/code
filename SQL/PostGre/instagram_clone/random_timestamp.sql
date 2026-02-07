-- 1. Randomize Users (Joined anytime in the last 12 months)
UPDATE users 
SET created_at = NOW() - (random() * INTERVAL '365 days');

-- 2. Randomize Posts (Must be created AFTER the user joined)
UPDATE posts 
SET created_at = users.created_at + (random() * (NOW() - users.created_at))
FROM users 
WHERE posts.user_id = users.id;

ALTER TABLE followers ADD COLUMN created_at TIMESTAMP DEFAULT NOW();
ALTER TABLE likes ADD COLUMN created_at TIMESTAMP DEFAULT NOW();
ALTER TABLE comments ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

-- 3. Randomize Followers (Must be created AFTER the follower joined)
UPDATE followers 
SET created_at = users.created_at + (random() * (NOW() - users.created_at))
FROM users 
WHERE followers.follower_id = users.id;

-- 4. Randomize Likes & Comments (Must be created AFTER the post was made)
UPDATE likes 
SET created_at = posts.created_at + (random() * (NOW() - posts.created_at))
FROM posts 
WHERE likes.post_id = posts.id;

UPDATE comments 
SET created_at = posts.created_at + (random() * (NOW() - posts.created_at))
FROM posts 
WHERE comments.post_id = posts.id;

SELECT 
    created_at::DATE as day, 
    COUNT(*) as activity_count
FROM (
    SELECT created_at FROM posts
    UNION ALL
    SELECT created_at FROM likes
    UNION ALL
    SELECT created_at FROM comments
) activity
GROUP BY day
ORDER BY day DESC
LIMIT 15;