-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES 
('Claudia Velasco Ortiz', 'claudia.velasco.o@enlace.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 11:01:45.152239'),
('Samuel Torres Galdós', 's.torres.g@construye.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 11:01:14.73627'),
('Natalia Salazar Mora', 'n.salazar.mora@vanguardia.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 11:00:54.00541'),
('Fernando Ríos Vargas', 'f.rios.vargas@ciencias.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 11:00:19.502115'),
('Isabel Quintana Rojas', 'i.quintana.r@estilo.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:59:46.229776'),
('Nicolás Paredes Méndez', 'n.paredes.m@red.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:58:47.950621'),
('Beatriz Olivares Guerra', 'b.olivares.g@comunicaciones.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:57:19.289225'),
('Diego Navarro Duque', 'diego.navarro.d@empresa.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:56:31.484701'),
('Camila Montoya Serrano', 'c.montoya.s@academia.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:54:09.835121'),
('Hugo Lozano Castillo', 'h.lozano.c@webmail.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:53:29.88208'),
('Valeria Jiménez Bravo', 'v.jimenez.bravo@diseno.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:52:34.877831'),
('Sebastián Ibarra Flores', 'sibarra.flores@consultoria.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:51:19.345618'),
('Sofía Heredia Nazario', 's.heredia.n@nube.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:50:08.909081'),
('Adrián Gallego Santos', 'adrian.gallego.s@servicios.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:48:38.17962'),
('Martina Ferrer Blanco', 'martina.ferrer.b@global.com', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:48:00.843837'),
('Rodrigo Escudero Peña', 'r.escudero.p@proyectos.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:46:56.982686'),
('Elena De la Cruz Montes', 'elena.delacruz.m@estudio.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:45:26.014548'),
('Mateo Castañeda Vidal', 'm.castaneda.vidal@red.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:44:30.471195'),
('Lucía Beltrán Orozco', 'lucia.beltran.o@correo.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:43:22.431161'),
('Javier Alarcón Ruiz', 'j.alarcon.ruiz@ficticia.es', '', 'Tarifa', 'Spain', 'LOCAL', '2026-03-08 10:42:46.701391');

-- Note: If you are using PostgreSQL and want to update the ID sequence after these manual inserts:
-- SELECT setval('core_customer_id_seq', (SELECT MAX(id) FROM core_customer));
