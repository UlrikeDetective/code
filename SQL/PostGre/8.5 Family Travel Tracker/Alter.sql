ALTER TABLE public.student
RENAME TO users;

ALTER TABLE public.users
RENAME TO students;

Select * FROM public.students;

Alter table public.students
	alter column first_name Type Varchar(20);