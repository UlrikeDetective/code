-- Insert sample posts
INSERT INTO posts (user_id, image_url, caption) VALUES
(1, 'https://example.com/image1.jpg', 'First post by User One'),
(2, 'https://example.com/image2.jpg', 'Exciting post from User Two'),
(3, 'https://example.com/image3.jpg', 'Great vibes! #life'),
(4, 'https://example.com/image4.jpg', 'Final post for testing.'),
(1, 'https://example.com/image1.jpg', 'Chilling in the Arctic 🐧'),
(9, 'https://example.com/image2.jpg', 'Skyline dreams! 🌃'),
(3, 'https://example.com/image3.jpg', 'Another peak conquered 🏔️'),
(3, 'https://example.com/image20.jpg', 'This is just the beginning...');

INSERT INTO posts (user_id, image_url, caption)
VALUES (3, 'https://example.com/image21.jpg', 'Another peak conquered 🏔️');


SELECT * FROM posts WHERE user_id = 1;

UPDATE posts
SET caption = 'Updated caption for this awesome post!'
WHERE id = 1;

DELETE FROM posts WHERE id = 20;

