CREATE TABLE visited_countries(
id SERIAL PRIMARY KEY,
country_code CHAR(2) NOT NULL,
user_id INTEGER REFERENCES users(id)
);

INSERT INTO visited_countries (country_code, user_id)
VALUES ('FR', 5), ('GB', 5), ('CA', 6), ('BR', 6 );

SELECT *
FROM public.visited_countries
JOIN public.users
ON users.id = user_id;
