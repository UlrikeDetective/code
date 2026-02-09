-- SEEDING DATA FOR IMPROVED SCHEMA --

-- 1. Authors (Extracted from all available book data)
INSERT INTO authors (first_name, last_name) VALUES 
('Jhumpa', 'Lahiri'),
('Neil', 'Gaiman'),
('Dave', 'Eggers'),
('Michael', 'Chabon'),
('Patti', 'Smith'),
('Raymond', 'Carver'),
('Don', 'DeLillo'),
('John', 'Steinbeck'),
('David', 'Foster Wallace'),
('Toshikazu', 'Kawaguchi'),
('DK', 'Travel'),
('Toby', 'Neal'),
('Naomi', 'Klein'),
('Osamu', 'Dazai'),
('Stephanie', 'Land'),
('Monica', 'Ali'),
('Rolf', 'Potts'),
('Walter', 'Travis'),
('Nick', 'Hornby'),
('Sue', 'Monk Kidd'),
('Nanoko', 'Hanada'),
('Sally', 'Rooney'),
('Siri', 'Hustvedt'),
('Sayaka', 'Murata'),
('Alan', 'Watts'),
('Zz', 'Packer'),
('Claire', 'Keagan'),
('Illaria', 'Bernardini'),
('Musa', 'Okwonga'),
('Hannah', 'Fry'),
('Gabrielle', 'Zevin'),
('Dan', 'Harris'),
('Freida', 'Harris'),
('Emily', 'Henry'),
('Lauren', 'Graham'),
('Kevin', 'Kwan'),
('Pamela', 'Redmond Satran'),
('George', 'Saunders');

-- 2. Genres
INSERT INTO genres (name) VALUES 
('Fiction'), 
('Non-Fiction'), 
('Fantasy'), 
('Short Stories'),
('Memoir'),
('Travel'),
('Thriller'),
('Romance');

-- 3. Books (Mapping data to new tables with estimated prices)
-- Authors (IDs mapping):
-- 1:Lahiri, 2:Gaiman, 3:Eggers, 4:Chabon, 5:Smith, 6:Carver, 7:DeLillo, 8:Steinbeck, 9:Wallace, 
-- 10:Kawaguchi, 11:Travel, 12:Neal, 13:Klein, 14:Dazai, 15:Land, 16:Ali, 17:Potts, 18:Travis, 
-- 19:Hornby, 20:Monk Kidd, 21:Hanada, 22:Rooney, 23:Hustvedt, 24:Murata, 25:Watts, 26:Packer, 
-- 27:Keagan, 28:Bernardini, 29:Okwonga, 30:Fry, 31:Zevin, 32:D.Harris, 33:F.Harris, 34:Henry, 
-- 35:Graham, 36:Kwan, 37:Satran, 38:Saunders

-- Genres: 1:Fiction, 2:Non-Fiction, 3:Fantasy, 4:Short Stories, 5:Memoir, 6:Travel, 7:Thriller, 8:Romance

INSERT INTO books (title, author_id, genre_id, released_year, price, stock_quantity, pages) VALUES 
('The Namesake', 1, 1, 2003, 14.99, 32, 291),
('Norse Mythology', 2, 3, 2016, 18.50, 43, 304),
('American Gods', 2, 2, 2001, 22.00, 12, 465),
('Interpreter of Maladies', 1, 4, 1996, 12.95, 97, 198),
('A Hologram for the King: A Novel', 3, 1, 2012, 16.00, 154, 352),
('The Circle', 3, 1, 2013, 15.50, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 4, 1, 2000, 19.95, 68, 634),
('Just Kids', 5, 5, 2010, 14.50, 55, 304),
('A Heartbreaking Work of Staggering Genius', 3, 5, 2001, 17.00, 104, 437),
('Coraline', 2, 3, 2003, 11.99, 100, 208),
('What We Talk About When We Talk About Love: Stories', 6, 4, 1981, 13.00, 23, 176),
('Where I''m Calling From: Selected Stories', 6, 4, 1989, 15.50, 12, 526),
('White Noise', 7, 1, 1985, 14.00, 49, 320),
('Cannery Row', 8, 1, 1945, 10.99, 95, 181),
('Oblivion: Stories', 9, 4, 2004, 16.50, 172, 329),
('Before the coffee gets cold', 10, 1, 2015, 12.99, 23, 201),
('Tales from the cafe', 10, 1, 2017, 13.50, 32, 221),
('Before your memory fades', 10, 1, 2020, 14.00, 12, 223),
('Be more Japan', 11, 6, 2021, 25.00, 15, 340),
('Paradise Crime Thrillers - Vol 01 - Wired in', 12, 7, 2012, 9.99, 8, 351),
('Doppelganger', 13, 2, 2025, 26.00, 42, 427),
('Osamu Dazai Best Short Stories', 14, 4, 2011, 11.50, 11, 167),
('Maid', 15, 5, 2018, 16.00, 15, 437),
('Love Marriage', 16, 1, 2023, 22.00, 42, 428),
('The Vagabonds Way', 17, 6, 2023, 18.00, 4, 390),
('The Queens Gambit', 18, 1, 1984, 12.99, 8, 439),
('Just like you', 19, 1, 2019, 15.00, 5, 277),
('The secret life of bees', 20, 1, 2022, 14.00, 11, 429),
('The Bookshop Woman', 21, 1, 2021, 13.50, 3, 274),
('Intermezzo', 22, 1, 2025, 28.00, 12, 391),
('Mr Salary', 22, 1, 2021, 8.00, 2, 173),
('What I loved', 23, 1, 2005, 14.50, 3, 428),
('The summer without men', 23, 1, 2008, 15.00, 9, 451),
('Convenience Store Woman', 24, 1, 2022, 12.00, 6, 210),
('The way of zen', 25, 2, 2008, 18.00, 5, 254),
('Drinking Coffee elsewhere', 26, 4, 2013, 14.00, 9, 302),
('Antarctica', 27, 4, 2019, 13.00, 3, 183),
('Forster', 27, 1, 2016, 10.00, 19, 83),
('The girls are good', 28, 1, 2003, 16.00, 7, 418),
('One of Them', 29, 5, 2019, 17.00, 11, 402),
('Hello World', 30, 2, 2021, 19.99, 6, 426),
('Tomorrow, tomorrow, and tomorrow', 31, 1, 2023, 24.00, 12, 439),
('Consider the Lobster', 9, 2, 2005, 15.95, 92, 343),
('10% Happier', 32, 2, 2014, 12.00, 29, 256), 
('fake_book', 33, 1, 2001, 5.00, 287, 428),
('Beach read', 34, 8, 2014, 14.00, 35, 361),
('Talking as Fast As I can', 35, 5, 2018, 15.50, 5, 193),
('Crazy rich asians', 36, 1, 2011, 16.99, 25, 316),
('Younger', 37, 1, 2001, 12.99, 17, 357),
('Lincoln In The Bardo', 38, 1, 2017, 24.99, 1000, 367);

-- 4. Sample Customers
INSERT INTO customers (first_name, last_name, email) VALUES 
('Boy', 'George', 'george@gmail.com'),
('George', 'Michael', 'gm@gmail.com'),
('David', 'Bowie', 'david@gmail.com'),
('Blue', 'Steele', 'blue@gmail.com'),
('Bette', 'Davis', 'bette@aol.com');

-- 5. Sample Orders & Order Items
INSERT INTO orders (customer_id, total_amount) VALUES (1, 18.50);
INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES (1, 2, 1, 18.50);

INSERT INTO orders (customer_id, total_amount) VALUES (3, 50.00);
INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES 
(2, 3, 1, 22.00),
(2, 30, 1, 28.00);

-- 6. Sample Reviews
INSERT INTO reviews (book_id, customer_id, rating, comment) VALUES 
(2, 3, 5, 'Gaiman at his best with mythology!'),
(30, 2, 5, 'Rooney''s latest is a masterpiece.');