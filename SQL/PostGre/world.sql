CREATE TABLE public.flags (
    id integer NOT NULL,
    name character varying(45),
    flag text
);

Copy flags (id, name, flag)
FROM '/SQL_code/SQL/PostGre/flags.csv' DELIMITER ',' CSV HEADER;

select * from flags;

CREATE TABLE public.countries (
    id integer NOT NULL,
    country_code character(2),
    country_name character(100)
);

Copy countries (id, country_code, country_name)
FROM '/SQL_code/SQL/PostGre/countries.csv' DELIMITER ',' CSV HEADER;

select * from countries;

CREATE TABLE public.capitals (
    id integer NOT NULL,
    country character varying(45),
    capital character varying(45)
);

COPY capitals (id, country, capital)
FROM '/SQL_code/SQL/PostGre/capitals.csv' DELIMITER ',' CSV HEADER;

select * from capitals;

CREATE TABLE public.users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(15) UNIQUE NOT NULL,
	color VARCHAR(15)
);

-- drop table users;

INSERT INTO users (name, color)
VALUES ('All', 'teal'), ('Wishlist', 'powderblue');

INSERT INTO users (name, color)
VALUES ('Bee', 'lemon'), ('wasp', 'black'), ('lion', 'golden'), ('butterfly', 'yellow'), ('sloth', 'cornflower'), ('whale', 'grey');

-- DELETE FROM public.users

Select * From public.users

CREATE TABLE public.visited_countries (
	id SERIAL PRIMARY KEY,
	country_code CHAR(2) NOT NULL,
	user_id INTEGER REFERENCES users(id)
);

-- drop table visited_countries;

INSERT INTO visited_countries (country_code, user_id)
VALUES ('FR', 5), ('GB', 5), ('CA', 6), ('BR', 6 );

SELECT *
FROM public.visited_countries
JOIN public.users
ON users.id = user_id;