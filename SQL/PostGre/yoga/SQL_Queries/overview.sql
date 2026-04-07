select * from auth_group;
select * from auth_group_permissions;
select * from auth_permission;
select * from auth_user;
select * from auth_user_groups;
select * from auth_user_user_permissions;
select * from core_customer order by id desc;
select * from core_expense;
select * from core_inventory;
select * from core_lesson;
select * from core_lesson_attendees;
select * from core_package;
select * from django_admin_log;
select * from django_content_type;
select * from django_migrations;
select * from django_session;


select * from core_customer where name = 'Ava Dubois';
select * from core_customer where country = 'Spain';
select * from core_customer where city = 'Tarifa';

UPDATE core_customer
SET country = 'United Kingdom'
WHERE country = 'UK';

-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES
('Francisco Javier García', 'javier.garcia@example.es', '+34910000001', 'Madrid', 'Spain', 'VISITOR', NOW()),
('María Carmen Rodríguez', 'marmen.rodriguez@example.es', '+34930000002', 'Barcelona', 'Spain', 'VISITOR', NOW()),
('José Antonio Martínez', 'jose.martinez@example.es', '+34950000003', 'Seville', 'Spain', 'VISITOR', NOW()),
('Montserrat Puig', 'montserrat.puig@example.es', '+34930000004', 'Girona', 'Spain', 'VISITOR', NOW()),
('Jordi Molins', 'jordi.molins@example.es', '+34930000005', 'Lleida', 'Spain', 'VISITOR', NOW()),
('Alejandro Sanz', 'alejandro.sanz@example.es', '+34910000006', 'Madrid', 'Spain', 'VISITOR', NOW()),
('Lucía Fernández', 'lucia.fernandez@example.es', '+34960000007', 'Valencia', 'Spain', 'VISITOR', NOW()),
('David López', 'david.lopez@example.es', '+34950000008', 'Málaga', 'Spain', 'VISITOR', NOW()),
('Paula Sánchez', 'paula.sanchez@example.es', '+34970000009', 'Zaragoza', 'Spain', 'VISITOR', NOW()),
('Iker Etxeberria', 'iker.etxeberria@example.es', '+34940000010', 'Bilbao', 'Spain', 'VISITOR', NOW()),
('Ainhoa Ortiz', 'ainhoa.ortiz@example.es', '+34940000011', 'San Sebastián', 'Spain', 'VISITOR', NOW()),
('Iago Castro', 'iago.castro@example.es', '+34980000012', 'Vigo', 'Spain', 'VISITOR', NOW()),
('Sara Ruiz', 'sara.ruiz@example.es', '+34950000013', 'Granada', 'Spain', 'VISITOR', NOW()),
('Daniel Gómez', 'daniel.gomez@example.es', '+34960000014', 'Alicante', 'Spain', 'VISITOR', NOW()),
('Alba Jiménez', 'alba.jimenez@example.es', '+34950000015', 'Córdoba', 'Spain', 'VISITOR', NOW()),
('Adrián Moreno', 'adrian.moreno@example.es', '+34980000016', 'A Coruña', 'Spain', 'VISITOR', NOW()),
('Marta Muñoz', 'marta.munoz@example.es',+'34910550018', 'Valladolid', 'Spain', 'VISITOR', NOW()),
('Álvaro Pérez', 'alvaro.perez@example.es', '+34910000018', 'Madrid', 'Spain', 'VISITOR', NOW()),
('Isabel Díaz', 'isabel.diaz@example.es', '+34920000019', 'Murcia', 'Spain', 'VISITOR', NOW()),
('Juan Carlos Toro', 'juan.toro@example.es','+34920330019', 'Palma', 'Spain', 'VISITOR', NOW()),
('Raquel Serrano', 'raquel.serrano@example.es', '+34920000021', 'Las Palmas', 'Spain', 'VISITOR', NOW()),
('Rubén Hernández', 'ruben.hernandez@example.es', '+34920000022', 'Santa Cruz de Tenerife', 'Spain', 'VISITOR', NOW()),
('Nerea Blanco', 'nerea.blanco@example.es', '+34940000023', 'Vitoria-Gasteiz', 'Spain', 'VISITOR', NOW()),
('Sergio Navarro', 'sergio.navarro@example.es', '+34940000024', 'Pamplona', 'Spain', 'VISITOR', NOW()),
('Cristina Morales', 'cristina.morales@example.es', '+34920310019', 'Oviedo', 'Spain', 'VISITOR', NOW()),
('Borja Domínguez', 'borja.dominguez@example.es', '+34927600019', 'Santander', 'Spain', 'VISITOR', NOW()),
('Esther Vázquez', 'esther.vazquez@example.es', '+34980000027', 'Ourense', 'Spain', 'VISITOR', NOW()),
('Iván Ramos', 'ivan.ramos@example.es', '+34920000028', 'Badajoz', 'Spain', 'VISITOR', NOW()),
('Silvia Gil', 'silvia.gil@example.es', '+34920240019', 'logrono', 'Spain', 'VISITOR', NOW()),
('Oscar Ramirez', 'oscar.ramirez@example.es', '+34920000030', 'Salamanca', 'Spain', 'VISITOR', NOW()),
('Beatriz Soto', 'beatriz.soto@example.es', '+34920037019', 'Burgos', 'Spain', 'VISITOR', NOW()),
('Hugo Ibáñez', 'hugo.ibanez@example.es', '+34960000032', 'Castellón', 'Spain', 'VISITOR', NOW()),
('Noelia Ferrer', 'noelia.ferrer@example.es', '+34920079019', 'Tarragona', 'Spain', 'VISITOR', NOW()),
('Manuel Soler', 'manuel.soler@example.es', '+34950000034', 'Almería', 'Spain', 'VISITOR', NOW()),
('Lorena Garrido', 'lorena.garrido@example.es', '+34950000035', 'Huelva', 'Spain', 'VISITOR', NOW()),
('Víctor León', 'victor.leon@example.es', '+34950000036', 'Cádiz', 'Spain', 'VISITOR', NOW()),
('Patricia Calvo', 'patricia.calvo@example.es', '+34910000037', 'Alcalá de Henares', 'Spain', 'VISITOR', NOW()),
('Ignacio Reyes', 'ignacio.reyes@example.es', '+34910000038', 'Getafe', 'Spain', 'VISITOR', NOW()),
('Yolanda Herrera', 'yolanda.herrera@example.es', '+34930000039', 'Sabadell', 'Spain', 'VISITOR', NOW()),
('Felipe Vidal', 'felipe.vidal@example.es', '+34930000040', 'Terrassa', 'Spain', 'VISITOR', NOW()),
('Andrea Marin', 'andrea.marin@example.es', '+34960000041', 'Elche', 'Spain', 'VISITOR', NOW()),
('Santiago Peinado', 'santiago.peinado@example.es', '+34950000042', 'Jaén', 'Spain', 'VISITOR', NOW()),
('Verónica Parra', 'veronica.parra@example.es', '+34920081019', 'Alcorcón', 'Spain', 'VISITOR', NOW()),
('Guillermo Bravo', 'guillermo.bravo@example.es', '+34920876019', 'Fuenlabrada', 'Spain', 'VISITOR', NOW()),
('Clara Cabrera', 'clara.cabrera@example.es', '+34920020019', 'Leganés', 'Spain', 'VISITOR', NOW()),
('Luis Miguel Flores', 'luis.flores@example.es', '+34950000046', 'Marbella', 'Spain', 'VISITOR', NOW()),
('Inmaculada Romero', 'inmaculada.romero@example.es', '+34950000047', 'Dos Hermanas', 'Spain', 'VISITOR', NOW()),
('Rafael Vega', 'rafael.vega@example.es', '+34950000048', 'Jerez de la Frontera', 'Spain', 'VISITOR', NOW()),
('Natalia Méndez', 'natalia.mendez@example.es', '+34920300019', 'Cartagena', 'Spain', 'VISITOR', NOW()),
('Fernando Nieto', 'fernando.nieto@example.es', '+34920004019', 'Torrejón de Ardoz', 'Spain', 'VISITOR', NOW()),
('Miriam Castillo', 'miriam.castillo@example.es', '+34920200019', 'Parla', 'Spain', 'VISITOR', NOW()),
('Gonzalo Ortega', 'gonzalo.ortega@example.es', '+34923000019', 'lcobendas', 'Spain', 'VISITOR', NOW()),
('Elena Márquez', 'elena.marquez@example.es', '+34930000053', 'Badalona', 'Spain', 'VISITOR', NOW()),
('Joan Martí', 'joan.marti@example.es', '+34930000054', 'L''Hospitalet', 'Spain', 'VISITOR', NOW()),
('Carla Gallego', 'carla.gallego@example.es', '+34960000055', 'Torrent', 'Spain', 'VISITOR', NOW()),
('Antonio José Cruz', 'antonio.cruz@example.es', '+34920000056', 'Cáceres', 'Spain', 'VISITOR', NOW()),
('Inés Santos', 'ines.santos@example.es', '+34921000019', 'León', 'Spain', 'VISITOR', NOW()),
('Mario Montero', 'mario.montero@example.es', '+34927650019', 'Algeciras', 'Spain', 'VISITOR', NOW()),
('Lourdes Hidalgo', 'lourdes.hidalgo@example.es', '+34980000059', 'Santiago de Compostela', 'Spain', 'VISITOR', NOW()),
('Marcos Giménez', 'marcos.gimenez@example.es', '+34910000060', 'Madrid', 'Spain', 'VISITOR', NOW()),
('Rocío Ibáñez', 'rocio.ibanez@example.es', '+34930000061', 'Barcelona', 'Spain', 'VISITOR', NOW()),
('Emilio Serra', 'emilio.serra@example.es', '+34930000062', 'Reus', 'Spain', 'VISITOR', NOW()),
('Begoña Arellano', 'begona.arellano@example.es', '+34940000063', 'Barakaldo', 'Spain', 'VISITOR', NOW()),
('Mireia Blanch', 'mireia.blanch@example.es', '+34930000085', 'Cornellà', 'Spain', 'VISITOR', NOW()),
('Eneko Agirre', 'eneko.agirre@example.es', '+34940000086', 'Getxo', 'Spain', 'VISITOR', NOW());

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

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES
('Agata Nowak', 'agata.nowak@example.pl', '+48600100301', 'Łódź', 'Poland', 'VISITOR', NOW()),
('Piotr Pawlak', 'piotr.pawlak@example.pl', '+48600100302', 'Szczecin', 'Poland', 'VISITOR', NOW()),
('Magdalena Wójcik', 'magdalena.wojcik@example.pl', '+48600100303', 'Bydgoszcz', 'Poland', 'VISITOR', NOW()),
('Krzysztof Mazurek', 'krzysztof.mazurek@example.pl', '+48600100304', 'Lublin', 'Poland', 'VISITOR', NOW()),
('Ewa Kaczmarczyk', 'ewa.kaczmarczyk@example.pl', '+48600100305', 'Białystok', 'Poland', 'VISITOR', NOW()),
('Tomasz Krawczyk', 'tomasz.krawczyk@example.pl', '+48600100306', 'Katowice', 'Poland', 'VISITOR', NOW()),
('Anna Adamczyk', 'anna.adamczyk@example.pl', '+48600100307', 'Gdynia', 'Poland', 'VISITOR', NOW()),
('Michał Dudek', 'michal.dudek@example.pl', '+48600100308', 'Częstochowa', 'Poland', 'VISITOR', NOW()),
('Katarzyna Zając', 'katarzyna.zajac@example.pl', '+48600100309', 'Radom', 'Poland', 'VISITOR', NOW()),
('Andrzej Król', 'andrzej.krol@example.pl', '+48600100310', 'Sosnowiec', 'Poland', 'VISITOR', NOW()),
('Małgorzata Wieczorek', 'malgorzata.wieczorek@example.pl', '+48600100311', 'Toruń', 'Poland', 'VISITOR', NOW()),
('Paweł Wróbel', 'pawel.wrobel@example.pl', '+48600100312', 'Kielce', 'Poland', 'VISITOR', NOW()),
('Barbara Majewska', 'barbara.majewska@example.pl', '+48600100313', 'Gliwice', 'Poland', 'VISITOR', NOW()),
('Marcin Olszewski', 'marcin.olszewski@example.pl', '+48600100314', 'Zabrze', 'Poland', 'VISITOR', NOW()),
('Alicja Stępień', 'alicja.stepien@example.pl', '+48600100315', 'Olsztyn', 'Poland', 'VISITOR', NOW()),
('Jakub Jaworski', 'jakub.jaworski@example.pl', '+48600100316', 'Bielsko-Biała', 'Poland', 'VISITOR', NOW()),
('Dorota Malinowska', 'dorota.malinowska@example.pl', '+48600100317', 'Rzeszów', 'Poland', 'VISITOR', NOW()),
('Łukasz Nowicki', 'lukasz.nowicki@example.pl', '+48600100318', 'Ruda Śląska', 'Poland', 'VISITOR', NOW()),
('Marta Witkowska', 'marta.witkowska@example.pl', '+48600100319', 'Rybnik', 'Poland', 'VISITOR', NOW()),
('Rafał Walczak', 'rafal.walczak@example.pl', '+48600100320', 'Tychy', 'Poland', 'VISITOR', NOW()),
('Zofia Sikora', 'zofia.sikora@example.pl', '+48600100321', 'Dąbrowa Górnicza', 'Poland', 'VISITOR', NOW()),
('Mateusz Baran', 'mateusz.baran@example.pl', '+48600100322', 'Płock', 'Poland', 'VISITOR', NOW()),
('Natalia Rutkowska', 'natalia.rutkowska@example.pl', '+48600100323', 'Elbląg', 'Poland', 'VISITOR', NOW()),
('Grzegorz Michalski', 'grzegorz.michalski@example.pl', '+48600100324', 'Gorzów Wielkopolski', 'Poland', 'VISITOR', NOW()),
('Beata Ostrowska', 'beata.ostrowska@example.pl', '+48600100325', 'Wałbrzych', 'Poland', 'VISITOR', NOW()),
('Kamil Barczyk', 'kamil.barczyk@example.pl', '+48600100326', 'Włocławek', 'Poland', 'VISITOR', NOW()),
('Urszula Kowalczyk', 'urszula.kowalczyk@example.pl', '+48600100327', 'Zielona Góra', 'Poland', 'VISITOR', NOW()),
('Damian Tomaszewski', 'damian.tomaszewski@example.pl', '+48600100328', 'Tarnów', 'Poland', 'VISITOR', NOW()),
('Karolina Pietrzak', 'karolina.pietrzak@example.pl', '+48600100329', 'Chorzów', 'Poland', 'VISITOR', NOW()),
('Robert Marciniak', 'robert.marciniak@example.pl', '+48600100330', 'Kalisz', 'Poland', 'VISITOR', NOW()),
('Patrycja Jasińska', 'patrycja.jasinska@example.pl', '+48600100331', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Artur Zawadzki', 'artur.zawadzki@example.pl', '+48600100332', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Elżbieta Sadowska', 'elzbieta.sadowska@example.pl', '+48600100333', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Szymon Bąk', 'szymon.bak@example.pl', '+48600100334', 'Słupsk', 'Poland', 'VISITOR', NOW()),
('Monika Jakóbiak', 'monika.jakobiak@example.pl', '+48600100335', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Dominik Chmielewski', 'dominik.chmielewski@example.pl', '+48600100336', 'Jastrzębie-Zdrój', 'Poland', 'VISITOR', NOW()),
('Renata Borkowska', 'renata.borkowska@example.pl', '+48600100337', 'Jelenia Góra', 'Poland', 'VISITOR', NOW()),
('Maciej Sawicki', 'maciej.sawicki@example.pl', '+48600100338', 'Nowy Sącz', 'Poland', 'VISITOR', NOW()),
('Justyna Sokołowska', 'justyna.sokolowska@example.pl', '+48600100339', 'Konin', 'Poland', 'VISITOR', NOW()),
('Sebastian Maciejewski', 'sebastian.maciejewski@example.pl', '+48600100340', 'Piotrków Trybunalski', 'Poland', 'VISITOR', NOW()),
('Iwona Kucharska', 'iwona.kucharska@example.pl', '+48600100341', 'Inowrocław', 'Poland', 'VISITOR', NOW()),
('Filip Gajewski', 'filip.gajewski@example.pl', '+48600100342', 'Mysłowice', 'Poland', 'VISITOR', NOW()),
('Paulina Sikorska', 'paulina.sikorska@example.pl', '+48600100343', 'Piła', 'Poland', 'VISITOR', NOW()),
('Wojciech Krajewski', 'wojciech.krajewski@example.pl', '+48600100344', 'Lubin', 'Poland', 'VISITOR', NOW()),
('Edyta Szulc', 'edyta.szulc@example.pl', '+48600100345', 'Ostrów Wielkopolski', 'Poland', 'VISITOR', NOW()),
('Patryk Głowacki', 'patryk.glowacki@example.pl', '+48600100346', 'Ostrowiec Świętokrzyski', 'Poland', 'VISITOR', NOW()),
('Wioletta Brzezińska', 'wioletta.brzezinska@example.pl', '+48600100347', 'Suwałki', 'Poland', 'VISITOR', NOW()),
('Mariusz Wysocki', 'mariusz.wysocki@example.pl', '+48600100348', 'Gniezno', 'Poland', 'VISITOR', NOW()),
('Kinga Wasilewska', 'kinga.wasilewska@example.pl', '+48600100349', 'Stargard', 'Poland', 'VISITOR', NOW()),
('Daniel Kaczmarczyk', 'daniel.kaczmarczyk@example.pl', '+48600100350', 'Głogów', 'Poland', 'VISITOR', NOW());