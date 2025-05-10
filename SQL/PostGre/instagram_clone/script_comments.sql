DO $$
DECLARE
    user_count INT;
    valid_posts INT[];
    comment_count INT := 100;
    i INT := 1;
    random_user INT;
    random_post INT;
    comment TEXT;
    comments_pool TEXT[] := ARRAY[
        -- English comments
        'Love this! ❤️', 
        'Amazing 😍', 
        'Wow!', 
        'So cool! 😎', 
        'Incredible 👏', 
        'Awesome shot!', 
        'Great vibes! ✨', 
        '🔥🔥🔥', 
        'Can’t believe it!', 
        'So beautiful 💕', 
        'Goals 😍', 
        'This is everything!', 
        'Simply stunning!', 
        'Such a mood! 😁', 
        'Obsessed!', 
        'Perfect! 🥰', 
        'Haha love it! 😂', 
        'Dreamy ✨', 
        'Need to try this!', 
        'Looks amazing!',
		'Beyond words! 🤯', 'Mind blown! 🤯', 'Epic! 🙌', 'So inspiring! 🌟', 'Cant stop staring! 👀', 'Pure perfection! 👌', 
		'Feeling blessed 🙏', 'Major heart eyes! 😍', 'Absolutely breathtaking! 😮', 'This is art! 🖼️', 'Total envy! 😒', 
		'Seriously though, how?! 🤔', 'Living for this! 🥳', 'Giving me life! 💃', 'Feeling all the feels! 🥺', 'Just wow! 🤩',
		'Beyond amazing! 🤩', 'This is exactly what I needed today! ❤️', 'Feeling so grateful for this moment. 🙏', 
		'Cant wait to try this out myself! 🤩', 'This is pure happiness in a picture. 🥰', 'Im so inspired by this! ✨', 
		'This is a dream come true. 💭', 'This is giving me major wanderlust. 🌍', 'Im speechless! 😮', 
		'This is the kind of content I live for. 🙌', 'Im so glad I stumbled upon this. 😊',
		'This is absolutely breathtaking! 😮 Im speechless.',
		'This is everything Ive ever wanted and more! 🤩',
		'Im so inspired by this! 🌟 Its truly amazing.',
		'This is giving me major feels! 🥺 So beautiful.',
		'I cant believe my eyes! 🤯 This is unreal.',
		'This is pure perfection! 👌 A masterpiece.', 'Great post!',
		'Im living for this vibe! ✨ So dreamy.', 'Loving the vibe!', 'Amazing work!',
		'This is the kind of content I live for! 🙌', 'Wow, amazing shot!', 'Final comment.', 'Looks awesome!',
		'Im so jealous of this! 😒 But also, so impressed.', 'You inspire me!', 'Epic capture 🔥', 'Love this view!',
		

        -- German comments
        'Wunderschön! 😍', 
        'So cool! 😎', 
        'Unglaublich! 👏', 
        'Toll gemacht! 😍', 
        'Das ist der Wahnsinn! 🔥', 
        'Ich liebe es! ❤️', 
        'Echt beeindruckend! 👏', 
        'So ein schöner Moment! 💖', 
        'Tolle Stimmung! ✨', 
        'Wirklich traumhaft! 🥰', 
        'Das gefällt mir! 😊', 
        'Einfach atemberaubend! 😱', 
        'Fantastisch! 🌟', 
        'Wow, das ist Kunst! 🎨', 
        'Absolut genial! 🤩', 
        'Ein echter Traum! ✨', 
        'Mega cool! 😎', 
        'Was für ein Moment! 💥',

        -- Spanish comments
        '¡Increíble! 😍', 
        '¡Qué bonito! 💖', 
        'Impresionante 👏', 
        '¡Me encanta! ❤️', 
        '¡Espectacular! 🌟', 
        'Qué hermoso 💕', 
        '¡Súper cool! 😎', 
        'Esto es arte 🎨', 
        '¡Esos colores! 😍', 
        '¡Wow! 😱', 
        'Esto es increíble 🔥', 
        '¡Qué vibes! ✨', 
        '¡Genial! 🥳', 
        '¡Perfecto! 👏', 
        '¡Amor puro! ❤️', 
        'Increíble fotografía 📸', 
        '¡Qué emoción! 😁', 
        '¡Esto es lo máximo! 🔥',

        -- French comments
        'Magnifique! 😍', 
        'C’est incroyable! 👏', 
        'Super cool! 😎', 
        'J’adore! ❤️', 
        'Quel moment magique! ✨', 
        'Incroyable 👏', 
        'Tellement beau! 💖', 
        'Wow, c’est génial! 😱', 
        'C’est un rêve! 💭', 
        'Époustouflant! 🌟', 
        'Quel talent! 🎨', 
        'Ça déchire! 😎', 
        'Trop bien! 😍', 
        'Je suis impressionné! 👏', 
        'C’est parfait! 🥰', 
        'Ça me fait rêver! ✨', 
        'Le meilleur! 🏆', 
        'J’aime trop! ❤️'
    ];
BEGIN
    -- Get the total number of users
    SELECT COUNT(*) INTO user_count FROM users;

    -- Get all valid post IDs as an array
    SELECT ARRAY(SELECT id FROM posts) INTO valid_posts;

    IF user_count = 0 OR array_length(valid_posts, 1) IS NULL THEN
        RAISE EXCEPTION 'No users or posts found in the database. Please ensure both tables are populated.';
    END IF;

    -- Generate comments
    WHILE i <= comment_count LOOP
        -- Select random user_id
        random_user := FLOOR(random() * user_count + 1)::INT;

        -- Select a random post_id from the valid list
        random_post := valid_posts[FLOOR(random() * array_length(valid_posts, 1) + 1)::INT];

        -- Select a random comment from the pool
        comment := comments_pool[FLOOR(random() * array_length(comments_pool, 1) + 1)];

        -- Insert into the comments table
        INSERT INTO comments (user_id, post_id, content)
        VALUES (random_user, random_post, comment)
        ON CONFLICT DO NOTHING;

        i := i + 1;
    END LOOP;
END $$;
