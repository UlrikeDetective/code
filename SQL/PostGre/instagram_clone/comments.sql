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


