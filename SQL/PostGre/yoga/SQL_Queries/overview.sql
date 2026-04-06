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
select * from core_customer where country = 'Denmark';

-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES
('Anne Jensen', 'anne.jensen@example.dk', '+4520100001', 'Copenhagen', 'Denmark', 'VISITOR', NOW()),
('Mette Nielsen', 'mette.nielsen@example.dk', '+4520100002', 'Aarhus', 'Denmark', 'VISITOR', NOW()),
('Camilla Hansen', 'camilla.hansen@example.dk', '+4520100003', 'Odense', 'Denmark', 'VISITOR', NOW()),
('Louise Pedersen', 'louise.pedersen@example.dk', '+4520100004', 'Aalborg', 'Denmark', 'VISITOR', NOW()),
('Maria Andersen', 'maria.andersen@example.dk', '+4520100005', 'Esbjerg', 'Denmark', 'VISITOR', NOW()),
('Emma Christensen', 'emma.christensen@example.dk', '+4520100006', 'Randers', 'Denmark', 'VISITOR', NOW()),
('Sofia Larsen', 'sofia.larsen@example.dk', '+4520100007', 'Kolding', 'Denmark', 'VISITOR', NOW()),
('Ida Sørensen', 'ida.sorensen@example.dk', '+4520100008', 'Horsens', 'Denmark', 'VISITOR', NOW()),
('Freja Rasmussen', 'freja.rasmussen@example.dk', '+4520100009', 'Vejle', 'Denmark', 'VISITOR', NOW()),
('Julie Jørgensen', 'julie.jorgensen@example.dk', '+4520100010', 'Roskilde', 'Denmark', 'VISITOR', NOW()),
('Lærke Madsen', 'laerke.madsen@example.dk', '+4520100011', 'Helsingør', 'Denmark', 'VISITOR', NOW()),
('Sara Kristensen', 'sara.kristensen@example.dk', '+4520100012', 'Herning', 'Denmark', 'VISITOR', NOW()),
('Nadia Olsen', 'nadia.olsen@example.dk', '+4520100013', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Yasmin Poulsen', 'yasmin.poulsen@example.dk', '+4520100014', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Leyla Knudsen', 'leyla.knudsen@example.dk', '+4520100015', 'Næstved', 'Denmark', 'VISITOR', NOW()),
('Amalie Møller', 'amalie.moller@example.dk', '+4520100016', 'Fredericia', 'Denmark', 'VISITOR', NOW()),
('Mathilde Johansen', 'mathilde.johansen@example.dk', '+4520100017', 'Viborg', 'Denmark', 'VISITOR', NOW()),
('Karoline Thomsen', 'karoline.thomsen@example.dk', '+4520100018', 'Køge', 'Denmark', 'VISITOR', NOW()),
('Peter Jensen', 'peter.jensen@example.dk', '+4520100019', 'Holstebro', 'Denmark', 'VISITOR', NOW()),
('Thomas Nielsen', 'thomas.nielsen@example.dk', '+4520100020', 'Taastrup', 'Denmark', 'VISITOR', NOW()),
('Michael Hansen', 'michael.hansen@example.dk', '+4520100021', 'Slagelse', 'Denmark', 'VISITOR', NOW()),
('Mikkel Pedersen', 'mikkel.pedersen@example.dk', '+4520100022', 'Tarifa', 'Spain', 'LOCALE', NOW()),
('Andreas Andersen', 'andreas.andersen@example.dk', '+4520100023', 'Sønderborg', 'Denmark', 'VISITOR', NOW()),
('Christian Christensen', 'christian.christensen@example.dk', '+4520100024', 'Svendborg', 'Denmark', 'VISITOR', NOW()),
('Mads Larsen', 'mads.larsen@example.dk', '+4520100025', 'Holbæk', 'Denmark', 'VISITOR', NOW()),
('Rasmus Sørensen', 'rasmus.sorensen@example.dk', '+4520100026', 'Hjørring', 'Denmark', 'VISITOR', NOW()),
('Magnus Rasmussen', 'magnus.rasmussen@example.dk', '+4520100027', 'Frederikshavn', 'Denmark', 'VISITOR', NOW()),
('Jonas Jørgensen', 'jonas.jorgensen@example.dk', '+4520100028', 'Copenhagen', 'Denmark', 'VISITOR', NOW()),
('Omar Bakir', 'omar.bakir@example.dk', '+4520100029', 'Aarhus', 'Denmark', 'VISITOR', NOW()),
('Emil Madsen', 'emil.madsen@example.dk', '+4520100030', 'Odense', 'Denmark', 'VISITOR', NOW());

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