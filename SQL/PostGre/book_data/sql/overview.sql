select * from authors;
select * from books order by id desc;
select * from genres;
select * from events;
select * from event_registrations;
select * from customers order by id desc;
select * from order_items order by id desc;
select * from orders order by id desc;
select * from reviews;


SELECT * FROM authors WHERE first_name = 'Toby';
Select * From books where author_id = 12;

INSERT INTO books (title, author_id, genre_id, released_year, price, stock_quantity, pages) VALUES
('Paradise Crime Thrillers - Vol 02 - Wired rogue', 12, 7, 2016, 9.99, 10, 297),
('Paradise Crime Thrillers - Vol 03 - Wired hard', 12, 7, 2017, 9.99, 10, 281),
('Paradise Crime Thrillers - Vol 04 - Wired dark', 12, 7, 2017, 9.99, 10, 279),
('Paradise Crime Thrillers - Vol 05 - Wired dawn', 12, 7, 2018, 9.99, 10, 299),
('Paradise Crime Thrillers - Vol 06 - Wired justice', 12, 7, 2018, 9.99, 10, 301),
('Paradise Crime Thrillers - Vol 07 - Wired secret', 12, 7, 2018, 9.99, 10, 283),
('Paradise Crime Thrillers - Vol 08 - Wired fear', 12, 7, 2019, 9.99, 10, 286),
('Paradise Crime Thrillers - Vol 10 - Wired courage', 12, 7, 2019, 9.99, 10, 298),
('Paradise Crime Thrillers - Vol 11 - Wired truth', 12, 7, 2020, 9.99, 10, 269),
('Paradise Crime Thrillers - Vol 12 - Wired ghost', 12, 7, 2020, 9.99, 10, 293),
('Paradise Crime Thrillers - Vol 13 - Wired strong', 12, 7, 2020, 9.99, 10, 295),
('Paradise Crime Thrillers - Vol 14 - Wired revenge', 12, 7, 2021, 9.99, 10, 284),
('Paradise Crime Thrillers - Vol 15 - Wired target', 12, 7, 2022, 9.99, 10, 293);