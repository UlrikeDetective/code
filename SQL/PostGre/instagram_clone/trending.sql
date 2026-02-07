WITH post_engagement AS (
    SELECT 
        p.id AS post_id,
        -- Weighing engagement: 1 like = 1 point, 1 comment = 3 points
        (COUNT(DISTINCT l.user_id) + (COUNT(DISTINCT c.id) * 3)) AS score
    FROM posts p
    LEFT JOIN likes l ON p.id = l.post_id
    LEFT JOIN comments c ON p.id = c.post_id
    -- Only look at posts from the last 7 days
    WHERE p.created_at >= NOW() - INTERVAL '7 days'
    GROUP BY p.id
)
SELECT 
    u.username,
    p.image_url,
    p.caption,
    p.created_at,
    pe.score AS trend_score
FROM posts p
JOIN post_engagement pe ON p.id = pe.post_id
JOIN users u ON p.user_id = u.id
ORDER BY pe.score DESC
LIMIT 10;


CREATE VIEW trending_feed AS
WITH post_engagement AS (
    SELECT 
        p.id AS post_id,
        -- Weighing engagement: 1 like = 1 point, 1 comment = 3 points
        (COUNT(DISTINCT l.user_id) + (COUNT(DISTINCT c.id) * 3)) AS score
    FROM posts p
    LEFT JOIN likes l ON p.id = l.post_id
    LEFT JOIN comments c ON p.id = c.post_id
    -- Only look at posts from the last 7 days
    WHERE p.created_at >= NOW() - INTERVAL '7 days'
    GROUP BY p.id
)
SELECT 
    u.username,
    p.image_url,
    p.caption,
    p.created_at,
    pe.score AS trend_score
FROM posts p
JOIN post_engagement pe ON p.id = pe.post_id
JOIN users u ON p.user_id = u.id
ORDER BY (pe.score / EXTRACT(EPOCH FROM (NOW() - p.created_at)/3600)) DESC
LIMIT 10;

select * from trending_feed;