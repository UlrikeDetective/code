Select * From public.contact_detail;

Update public.contact_detail
	Set email = 'hello@world.com'
	where id = 1;

Select * From public.contact_detail;