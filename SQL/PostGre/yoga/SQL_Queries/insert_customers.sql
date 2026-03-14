-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES 
('Claudia Velasco Ortiz', 'claudia.velasco.o@enlace.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 11:01:45.152239'),
('197,"Claudia","Romero Diez","claudia.romero.d@icloud.com","2026-03-11 20:11:14.345535"
196,"Sebastián","Vega Beltrán","sebv.escritor@gmail.com","2026-03-11 20:10:08.686101"
195,"Daniela","Aguilar Crespo","daniela.aguilar@telefonica.net","2026-03-11 20:08:48.052296"
194,"Ricardo","Ramos Suero","r.ramos.tarifa@proton.me","2026-03-11 20:07:14.25059"
193,"Valeria","Ferrer Domínguez","v.ferrer.lectura@gmail.com","2026-03-11 20:03:32.745996"
192,"Marcos","Serrano Peña","marcos_serrano_85@correo.es","2026-03-11 20:02:42.448751"
191,"Isabel","Ibáñez Torres","isa.ibanez@yahoo.com","2026-03-11 20:01:16.262143"
190,"Adrián","Lozano Gil","adri.lozano.books@outlook.es","2026-03-11 19:59:50.395408"
189,"Alba","Guerrero Pascual","alba.guerrero.p@me.com","2026-03-11 19:59:08.842034"
188,"Pablo","Cano Medina","pablo.cano.levante@gmail.com","2026-03-11 19:58:35.111634"
187,"Sofía","Lara Blanco","sofia.larab@gestion.es","2026-03-11 07:51:06.251457"
186,"Diego","Morales Ortega","diego.morales.surf@gmail.com","2026-03-11 07:50:30.218817"
185,"Elena","Vidal Garrido","elenavidal_92@hotmail.com","2026-03-11 07:49:54.98446"
184,"Javier","Méndez Rubio","javi.mendez.tarifa@protonmail.com","2026-03-11 07:49:11.368181"
183,"Martina","Navarro Soler","martina.nav@icloud.com","2026-03-11 07:48:39.218027"
182,"Hugo","Jiménez Castro","hugo_j_castro@yahoo.es","2026-03-11 07:43:56.298688"
181,"Carmen","Ortiz Núñez","carmen.ortiz@telefonica.net","2026-03-11 07:43:20.809546"
180,"Mateo","Ruiz Delgado","m.ruiz.vientos@outlook.com","2026-03-11 07:42:31.097654"
179,"Lucía","Fernández Santos","lucia.tarifabooks@gmail.com","2026-03-11 07:42:01.591589"
178,"Alejandro","García Marín","al.garcia88@correo.es","2026-03-11 07:40:24.760978"
176,"Lani","Nalu","paradisedream@example.com","2026-03-09 11:28:05.192474"')

-- Note: If you are using PostgreSQL and want to update the ID sequence after these manual inserts:
-- SELECT setval('core_customer_id_seq', (SELECT MAX(id) FROM core_customer));
