SELECT MAX(id) FROM comments;

Select * From comments;

-- Insert sample comments
INSERT INTO comments (user_id, post_id, content) VALUES
(1, 2, 'Great post!'), 
(2, 1, 'Amazing work!'), 
(3, 1, 'Loving the vibe!'), 
(1, 3, 'Looks awesome!'),
(4, 2, 'Final comment.'),
(9, 2, 'Wow, amazing shot!'), 
(9, 3, 'Love this view!'), 
(9, 4, 'Epic capture 🔥'),
(10, 4, 'You inspire me!');

INSERT INTO comments (user_id, post_id, content)
WITH comment_pool AS (
    SELECT UNNEST(ARRAY[
        'Great post!', 'Amazing work!', 'Loving the vibe!', 'Looks awesome!',
        'Wow, amazing shot!', 'Love this view!', 'Epic capture 🔥', 'You inspire me!',
        'This is pure goals ✨', 'Take me there! 😍', 'Unreal!', 'So dreamy...',
        'Keep killing it!', 'This is everything.', 'Best thing I’ve seen today.',
        'Absolutely stunning!', 'I need to visit here ASAP!', 'Pure magic. ✨',
        'Literal perfection.', 'Can we talk about how good this is?', 'No way!!',
        'Obsessed with this.', 'Stellar shot, friend!'
    ]) AS comment_text
),
random_engagement AS (
    -- Everyone has a chance to comment on random posts
    SELECT 
        u.id as user_id,
        p.id as post_id
    FROM users u
    CROSS JOIN LATERAL (
        SELECT id FROM posts 
        ORDER BY random() 
        LIMIT floor(random() * 2) -- Most users comment on 0-1 random posts
    ) p
    WHERE random() > 0.7 -- Only 30% of users are "active commenters"
),
influencer_engagement AS (
    -- Influencer posts get way more comments
    SELECT 
        u.id as user_id,
        p.id as post_id
    FROM users u
    CROSS JOIN LATERAL (
        SELECT p.id 
        FROM posts p
        JOIN (SELECT following_id FROM followers GROUP BY following_id ORDER BY COUNT(*) DESC LIMIT 15) i 
          ON p.user_id = i.following_id
        ORDER BY random()
        LIMIT 1
    ) p
    WHERE random() > 0.85 -- 15% chance to comment on a "viral" post
)
SELECT 
    engagement.user_id,
    engagement.post_id,
    (SELECT comment_text FROM comment_pool ORDER BY random() LIMIT 1)
FROM (
    SELECT * FROM random_engagement
    UNION ALL
    SELECT * FROM influencer_engagement
) engagement;

SELECT 
    p.id AS post_id, 
    u.username, 
    p.caption, 
    COUNT(c.id) AS comment_count
FROM posts p
JOIN users u ON p.user_id = u.id
JOIN comments c ON p.id = c.post_id
GROUP BY p.id, u.username
ORDER BY comment_count DESC
LIMIT 10;

-- List all comments on a specific post:
SELECT u.username, c.content, c.created_at
FROM comments c
JOIN users u ON c.user_id = u.id
WHERE c.post_id = 1;

-- Add a comment
INSERT INTO comments (user_id, post_id, content)
VALUES (11, 1, 'This is such a cool photo!');

-- Edit a comment
UPDATE comments
SET content = 'more of this'
WHERE id = 1;

-- Delete a comment
DELETE FROM comments WHERE id = 1;


