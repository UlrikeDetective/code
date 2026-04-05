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
select * from core_customer where country = 'Germany';

-- SQL query to insert local customers from Tarifa, Spain
-- Table: core_customer

INSERT INTO core_customer (name, email, phone, city, country, customer_type, created_at)
VALUES 
('Katharina Wagner', 'katharina.wagner@example.at', '+43 664 1234567', 'Vienna', 'Austria', 'VISITOR', NOW()),
('Julia Müller', 'j.mueller@testmail.at', '+43 676 2345678', 'Graz', 'Austria', 'VISITOR', NOW()),
('Lisa Pichler', 'lisa.pichler@pichler.at', '+43 650 3456789', 'Linz', 'Austria', 'VISITOR', NOW()),
('Melanie Steiner', 'm.steiner@example.at', '+43 660 4567890', 'Salzburg', 'Austria', 'VISITOR', NOW()),
('Laura Moser', 'laura.moser@moser.at', '+43 699 5678901', 'Innsbruck', 'Austria', 'VISITOR', NOW()),
('Nicole Hofer', 'n.hofer@test.at', '+43 664 6789012', 'Klagenfurt', 'Austria', 'VISITOR', NOW()),
('Elena Berger', 'elena.berger@berger.at', '+43 676 7890123', 'Villach', 'Austria', 'VISITOR', NOW()),
('Jasmin Fischer', 'j.fischer@fischer.at', '+43 650 8901234', 'Wels', 'Austria', 'VISITOR', NOW()),
('Verena Schmid', 'verena.schmid@example.at', '+43 660 9012345', 'Sankt Pölten', 'Austria', 'VISITOR', NOW()),
('Sabrina Weber', 's.weber@weber-logic.at', '+43 699 0123456', 'Dornbirn', 'Austria', 'VISITOR', NOW()),
('Sophie Reiter', 'sophie.reiter@reiter.at', '+43 664 1112233', 'Wiener Neustadt', 'Austria', 'VISITOR', NOW()),
('Hannah Winkler', 'h.winkler@winkler.at', '+43 676 2223344', 'Steyr', 'Austria', 'VISITOR', NOW()),
('Marlene Wallner', 'marlene.wallner@wallner.at', '+43 650 3334455', 'Feldkirch', 'Austria', 'VISITOR', NOW()),
('Viktoria Auer', 'v.auer@auer.at', '+43 660 4445566', 'Bregenz', 'Austria', 'VISITOR', NOW()),
('Kerstin Mayr', 'kerstin.mayr@mayr.at', '+43 699 5556677', 'Wolfsberg', 'Austria', 'VISITOR', NOW()),
('Emina Hadžić', 'emina.hadzic@hadzic.at', '+43 664 6667788', 'Baden', 'Austria', 'VISITOR', NOW()),
('Maria Nowak', 'm.nowak@nowak.at', '+43 676 7778899', 'Leoben', 'Austria', 'VISITOR', NOW()),
('Fatma Yıldız', 'fatma.yildiz@yildiz.at', '+43 650 8889900', 'Klosterneuburg', 'Austria', 'VISITOR', NOW()),
('Jelena Stojković', 'j.stojkovic@stojkovic.at', '+43 660 9990011', 'Traun', 'Austria', 'VISITOR', NOW()),
('Anja Kaufmann', 'anja.kaufmann@kaufmann.at', '+43 699 1113333', 'Krems', 'Austria', 'VISITOR', NOW()),
('Theresa Egger', 't.egger@egger.at', '+43 664 2224444', 'Leonding', 'Austria', 'VISITOR', NOW()),
('Valentina Leitner', 'v.leitner@leitner.at', '+43 676 3335555', 'Amstetten', 'Austria', 'VISITOR', NOW()),
('Magdalena Ebner', 'm.ebner@ebner.at', '+43 650 4446666', 'Kapfenberg', 'Austria', 'VISITOR', NOW()),
('Miriam Weiss', 'miriam.weiss@weiss.at', '+43 660 5557777', 'Lustenau', 'Austria', 'VISITOR', NOW()),
('Elif Demir', 'e.demir@demir.at', '+43 699 6668888', 'Mödling', 'Austria', 'VISITOR', NOW()),
('Sandra Brunner', 'sandra.brunner@brunner.at', '+43 664 7779999', 'Hallein', 'Austria', 'VISITOR', NOW()),
('Clara Schwarz', 'c.schwarz@schwarz.at', '+43 676 8880000', 'Kufstein', 'Austria', 'VISITOR', NOW()),
('Ivana Horvat', 'ivana.horvat@horvat.at', '+43 650 9991111', 'Traiskirchen', 'Austria', 'VISITOR', NOW()),
('Tamara Wolf', 'tamara.wolf@wolf.at', '+43 660 1112222', 'Schwechat', 'Austria', 'VISITOR', NOW()),
('Leyla Kurt', 'l.kurt@kurt.at', '+43 699 2223333', 'Braunau am Inn', 'Austria', 'VISITOR', NOW()),
('Petra Baumgartner', 'p.baumgartner@baumgartner.at', '+43 664 3334444', 'Ansfelden', 'Austria', 'VISITOR', NOW()),
('Amra Suljić', 'amra.suljic@suljic.at', '+43 676 4445555', 'Saalfelden', 'Austria', 'VISITOR', NOW()),
('Leonie Winkler', 'l.winkler@winkler-tech.at', '+43 650 5556666', 'Achenkirch', 'Austria', 'VISITOR', NOW()),
('Lukas Gruber', 'lukas.gruber@gruber.at', '+43 660 6667777', 'Tulln', 'Austria', 'VISITOR', NOW()),
('Thomas Huber', 't.huber@huber.at', '+43 699 7778888', 'Hohenems', 'Austria', 'VISITOR', NOW()),
('David Wagner', 'david.wagner@wagner.at', '+43 664 8889999', 'Spittal an der Drau', 'Austria', 'VISITOR', NOW()),
('Michael Müller', 'm.mueller@mueller.at', '+43 676 9990000', 'Telfs', 'Austria', 'VISITOR', NOW()),
('Stefan Pichler', 'stefan.pichler@pichler.at', '+43 650 1114444', 'Ternitz', 'Austria', 'VISITOR', NOW()),
('Alexander Steiner', 'a.steiner@steiner.at', '+43 660 2225555', 'Perchtoldsdorf', 'Austria', 'VISITOR', NOW()),
('Daniel Moser', 'd.moser@moser.at', '+43 699 3336666', 'Feldkirchen in Kärnten', 'Austria', 'VISITOR', NOW()),
('Andreas Hofer', 'a.hofer@hofer.at', '+43 664 4447777', 'Bludenz', 'Austria', 'VISITOR', NOW()),
('Christian Berger', 'c.berger@berger.at', '+43 676 5558888', 'Bad Ischl', 'Austria', 'VISITOR', NOW()),
('Philipp Fischer', 'p.fischer@fischer.at', '+43 650 6669999', 'Eisenstadt', 'Austria', 'VISITOR', NOW()),
('Edin Muratović', 'e.muratovic@muratovic.at', '+43 660 7770000', 'Gmunden', 'Austria', 'VISITOR', NOW()),
('Sebastian Schmid', 's.schmid@schmid.at', '+43 699 8881111', 'Schwaz', 'Austria', 'VISITOR', NOW()),
('Marko Jurić', 'marko.juric@juric.at', '+43 664 9992222', 'Achenkirch', 'Austria', 'VISITOR', NOW()),
('Mehmet Kaya', 'm.kaya@kaya.at', '+43 676 1113333', 'Lienz', 'Austria', 'VISITOR', NOW()),
('Florian Weber', 'f.weber@weber.at', '+43 650 2224444', 'Wörgl', 'Austria', 'VISITOR', NOW());

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