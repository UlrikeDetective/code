DO $$
DECLARE
    activity_choices TEXT[] := ARRAY['partying all weekend', 'hanging out with friends', 'playing in a band', 'modeling', 'shopping'];
    user_count INT := 100;
    i INT := 1;
    username TEXT;
    email TEXT;
    password TEXT := 'defaultpassword123'; -- Replace with securely hashed passwords in production
    full_name TEXT;
    bio TEXT;
BEGIN
    WHILE i <= user_count LOOP
        -- Generate random username and email
        username := 'user_' || i || '_' || FLOOR(random() * 1000)::TEXT;
        email := username || '@influencer.com';

        -- Generate random full name
        full_name := 'User ' || i || ' ' || chr(65 + FLOOR(random() * 26)::INT) || '.';

        -- Select a random activity for the bio
        bio := 'I enjoy ' || activity_choices[FLOOR(random() * array_length(activity_choices, 1)) + 1];

        -- Insert into the users table
        INSERT INTO users (username, email, password, full_name, bio)
        VALUES (username, email, password, full_name, bio);

        i := i + 1;
    END LOOP;
END $$;
