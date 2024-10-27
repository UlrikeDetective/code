Alter table public.visited_countries
	add unique(user_id, country_code);

Drop table if exits ...