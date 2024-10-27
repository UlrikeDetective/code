Select * From public.contact_detail;

Update public.contact_detail
	Set email = 'hello@world.com'
	where id = 1;

Select * From public.contact_detail;

INSERT INTO public.contact_detail (tel, address, email)
VALUES 
    ('+4412457573', '543 Sunset', 'sunset@world.com'),
    ('+4379325573', '1072 Sunrise', 'sunrise@world.com'),
    ('+4954745753', '63 Moon', 'moon@world.com'),
    ('+4865434563', '853 Galaxy', 'galaxy@world.com');

Select * From public.contact_detail;