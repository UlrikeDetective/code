-- Preventing Self-Follows

DELIMITER $$

CREATE TRIGGER prevent_self_follows
	BEFORE INSERT ON follows FOR EACH ROW
	BEGIN
		IF NEW.follower_id = NEW.followee_id
		THEN
			SIGNAL SQLSTATE '45000'
				SET MESSAGE_TEXT = 'Cannot follow yourself';
		END IF;
	END;
$$
DELIMITER ;

-- DELIMITER $$
-- CREATE TRIGGER create_unfollow
-- 	AFTER DELETE ON follows FOR EACH ROW
-- 	BEGIN
-- 		INSERT INTO unfollows(follower_id, followee_id),
--         Values(OLD.follower_id,OLD.followee_id);
-- 	END;
-- $$
-- DELIMITER;

DELIMITER $$
CREATE TRIGGER capture_unfollow
	AFTER DELETE ON follows FOR EACH ROW
	BEGIN
		INSERT INTO unfollows
		SET 
        follower_id = OLD.follower_id,
		followee_id = OLD.followee_id;
	END;
$$
DELIMITER ;