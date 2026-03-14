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
('Claudia Romero Diez', 'claudia.romero.d@icloud.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:11:14.345535'),
('Sebastián Vega Beltrán', 'sebv.escritor@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:10:08.686101'),
('Daniela Aguilar Crespo', 'daniela.aguilar@telefonica.net', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:08:48.052296'),
('Ricardo Ramos Suero', 'r.ramos.tarifa@proton.me', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:07:14.25059'),
('Valeria Ferrer Domínguez', 'v.ferrer.lectura@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:03:32.745996'),
('Marcos Serrano Peña', 'marcos_serrano_85@correo.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:02:42.448751'),
('Isabel Ibáñez Torres', 'isa.ibanez@yahoo.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 20:01:16.262143'),
('Adrián Lozano Gil', 'adri.lozano.books@outlook.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 19:59:50.395408'),
('Alba Guerrero Pascual', 'alba.guerrero.p@me.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 19:59:08.842034'),
('Pablo Cano Medina', 'pablo.cano.levante@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 19:58:35.111634'),
('Sofía Lara Blanco', 'sofia.larab@gestion.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:51:06.251457'),
('Diego Morales Ortega', 'diego.morales.surf@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:50:30.218817'),
('Elena Vidal Garrido', 'elenavidal_92@hotmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:49:54.98446'),
('Javier Méndez Rubio', 'javi.mendez.tarifa@protonmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:49:11.368181'),
('Martina Navarro Soler', 'martina.nav@icloud.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:48:39.218027'),
('Hugo Jiménez Castro', 'hugo_j_castro@yahoo.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:43:56.298688'),
('Carmen Ortiz Núñez', 'carmen.ortiz@telefonica.net', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:43:20.809546'),
('Mateo Ruiz Delgado', 'm.ruiz.vientos@outlook.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:42:31.097654'),
('Lucía Fernández Santos', 'lucia.tarifabooks@gmail.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:42:01.591589'),
('Alejandro García Marín', 'al.garcia88@correo.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-11 07:40:24.760978'),
('Lani Nalu', 'welcometoparadisedream@example.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-09 11:28:05.192474');

select * from core_customer where city = 'Tarifa';