select * from auth_group;
select * from auth_group_permissions;
select * from auth_permission;
select * from auth_user;
select * from auth_user_groups;
select * from auth_user_user_permissions;
select * from core_customer;
select * from core_expense;
select * from core_inventory;
select * from core_lesson;
select * from core_lesson_attendees;
select * from core_package;
select * from django_admin_log;
select * from django_content_type;
select * from django_migrations;
select * from django_session;


select * from core_customer order by id desc;

-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES 
('Leyla Weiss','leyla.weiss@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:16:26.37359'),
('Aileen Jenkins','aileen.jenkins@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:14:48.877888'),
('Jayda Osborn','jayda.osborn@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:13:32.95091'),
('Fletcher Blevins','fletcher.blevins@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:12:27.435111'),
('Anya Burch','anya.burch@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:10:52.927778'),
('Lilly Murillo','lilly.murillo@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:09:45.107127'),
('Emilee Haas','emilee.haas@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:07:51.966602'),
('Matteo Chambers','matteo.chambers@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:06:45.247365'),
('Jayda Joseph','jayda.joseph@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:05:37.083207'),
('Sarai Moon','sarai.moon@tarifa.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-23 20:04:34.751374');

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES 
('Søren Bakke', 'soren.kitesurf@nordicnet.no', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 09:15:22.451233'),
('Emma Whitlock', 'emma.wh.nomad@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 10:22:11.102344'),
('Lukas Müller', 'l.mueller.design@web.de', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 11:05:44.882190'),
('Chloé Lefebvre', 'chloe.tarifa@orange.fr', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 12:45:30.551002'),
('Jasper van der Meer', 'jasper.vdmeer@ziggo.nl', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 14:10:05.112233'),
('Aria Rossi', 'rossi.aria@libero.it', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 15:33:18.992831'),
('Oliver Smith', 'olliver.smith.uk@outlook.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-12 16:55:40.441552'),
('Freja Jensen', 'freja.j@danishmail.dk', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 08:20:12.662110'),
('Liam O’Connor', 'liam.kite.tarifa@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 09:12:33.771223'),
('Anika Sharma', 'anika.sharma.coder@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 10:45:01.332445'),
('Sebastian Meyer', 's.meyer.yoga@gmx.de', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 11:20:55.112998'),
('Zoë Williams', 'zoe.waves@icloud.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 13:05:44.221004'),
('Matteo Bianchi', 'm.bianchi@proton.me', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 14:50:18.552113'),
('Sofia Lindberg', 'sofia.swede@yahoo.se', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-13 16:22:30.991882'),
('Julian Bennett', 'jules.bennett@me.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 07:15:10.442331'),
('Noa Cohen', 'noa.cohen.tarifa@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 08:40:22.112665'),
('Klara Nowak', 'klara.n.art@wp.pl', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 09:12:55.772331'),
('Finn Gallagher', 'finn.g@irishabroad.ie', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 10:05:33.881220'),
('Yuki Tanaka', 'yuki.tanaka@tokyomail.jp', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 11:22:44.552119'),
('Isabella Costa', 'bella.costa@uol.com.br', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-14 12:45:11.992884');

select * from core_customer where city = 'Tarifa';