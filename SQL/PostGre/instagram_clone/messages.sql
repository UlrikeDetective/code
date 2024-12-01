-- Insert sample messages
INSERT INTO messages (sender_id, receiver_id, content) VALUES
(1, 2, 'Hey, how are you?'),
(2, 1, 'I am good, thanks!'),
(1, 3, 'What’s up?'),
(3, 1, 'Not much, you?'),
(4, 2, 'Catch you later!'),
(7, 2, 'Hey, check out my latest post!'), 
(7, 1, 'Looks awesome!'),
(9, 4, 'When are we catching up?'),
(9, 1, 'See you soon!');

-- List all messages between two users:
SELECT * 
FROM messages
WHERE (sender_id = 1 AND receiver_id = 2)
   OR (sender_id = 2 AND receiver_id = 1)
ORDER BY sent_at;

-- send a message
INSERT INTO messages (sender_id, receiver_id, content)
VALUES (1, 2, 'Hello, how are you?');

-- delete a message
DELETE FROM messages WHERE id = 1;

