Select * From public.contact_detail;

Update public.contact_detail
	Set email = 'hello@world.com'
	where id = 1;

Select * From public.contact_detail;

ALTER TABLE public.contact_detail
ALTER COLUMN id SET NOT NULL;

ALTER TABLE public.contact_detail
ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;

ALTER TABLE public.contact_detail
DROP CONSTRAINT contact_detail_id_fkey;

INSERT INTO public.contact_detail (tel, address, email)
VALUES 
    ('+4412457573', '543 Sunset', 'sunset@world.com'),
    ('+4379325573', '1072 Sunrise', 'sunrise@world.com'),
    ('+4954745753', '63 Moon', 'moon@world.com'),
    ('+4865434563', '853 Galaxy', 'galaxy@world.com');

INSERT INTO public.contact_detail (tel, address, email)
VALUES 
    ('+348737573', '43 New York', 'newyork@world.com'),
    ('+2379557573', '192 Los Angeles', 'losangeles@world.com'),
    ('+4955695753', '473 Seattle', 'seattle@world.com'),
    ('+4654344563', '875 San Francisco', 'sanfrancisco@world.com');

Select * From public.contact_detail;

Delete from public.contact_detail
	WHERE id != 1 OR id IS NULL;

Delete from public.contact_detail
	WHERE id = 1;