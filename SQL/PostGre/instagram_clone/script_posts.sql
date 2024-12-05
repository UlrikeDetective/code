-- Script to generate 300 additional entries for the `likes` table

-- Posts that should receive significantly more likes
WITH frequent_posts AS (
    SELECT unnest(ARRAY[1, 2, 3, 5, 10, 15, 20, 30, 50, 100, 200]) AS post_id
),
-- Generate random user_id and biased post_id
generated_likes AS (
    SELECT
        (SELECT floor(random() * 1626 + 1)::int) AS user_id, -- Random user_id between 1 and 1600
        (CASE 
            WHEN random() < 0.5 THEN (SELECT post_id FROM frequent_posts ORDER BY random() LIMIT 1) -- Bias towards frequent_posts
            ELSE floor(random() * 300 + 1)::int -- Random post_id between 1 and 300
        END) AS post_id
    FROM generate_series(1, 300) -- Generate 300 rows
),
-- Filter out duplicates
unique_likes AS (
    SELECT DISTINCT user_id, post_id FROM generated_likes
    WHERE NOT EXISTS (
        SELECT 1 FROM likes WHERE likes.user_id = generated_likes.user_id AND likes.post_id = generated_likes.post_id
    )
)
-- Insert into `likes` table
INSERT INTO likes (user_id, post_id)
SELECT user_id, post_id FROM unique_likes;
