DELETE FROM public.visited_countries

Select * From public.visited_countries

INSERT INTO visited_countries (country_code, user_id)
VALUES ('FR', 5), ('GB', 5), ('CA', 6), ('BR', 6 );

SELECT *
FROM visited_countries
JOIN users
ON users.id = user_id;