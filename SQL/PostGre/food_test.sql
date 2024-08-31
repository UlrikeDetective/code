SELECT wheat_production FROM public.world_food
WHERE country = 'China';

SELECT rice_production FROM public.world_food
WHERE country = 'China';

SELECT * From public.world_food;

SELECT country From public.world_food
Where wheat_production > 20;
