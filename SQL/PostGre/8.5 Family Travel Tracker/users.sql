DELETE FROM public.users

Select * From public.users

DROP TABLE IF EXISTS visited_countries, users;

CREATE TABLE users(
id SERIAL PRIMARY KEY,
name VARCHAR(15) UNIQUE NOT NULL,
color VARCHAR(15)
);

INSERT INTO users (name, color)
VALUES ('All', 'teal'), ('Wishlist', 'powderblue');