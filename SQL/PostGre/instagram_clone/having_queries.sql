SELECT post_id, COUNT(*) AS like_count
FROM likes
GROUP BY post_id
HAVING COUNT(*) > 5
ORDER BY like_count DESC;
