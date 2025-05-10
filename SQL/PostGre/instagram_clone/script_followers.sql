DO $$
DECLARE
    follower_id INT;
    following_id INT;
    i INT := 0;
BEGIN
    WHILE i < 200 LOOP
        -- Generate random follower and following IDs
        follower_id := FLOOR(random() * 1826 + 1)::INT;
        following_id := FLOOR(random() * 1826 + 1)::INT;

        -- Ensure they are not the same and the combination is unique
        IF follower_id != following_id THEN
            BEGIN
                INSERT INTO followers (follower_id, following_id)
                VALUES (follower_id, following_id);
                i := i + 1; -- Only increment if insertion succeeds
            EXCEPTION WHEN unique_violation THEN
                -- Skip duplicate entries
                CONTINUE;
            END;
        END IF;
    END LOOP;
END $$;
