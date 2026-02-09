-- CREATE TABLES --

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_fname VARCHAR(100),
    author_lname VARCHAR(100),
    released_year INT,
    stock_quantity INT,
    pages INT
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT REFERENCES customers(id)
);

-- INSERT DATA --

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman', 2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
('Where I''m Calling From: Selected Stories', 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Before the coffee gets cold', 'Toshikazu', 'Kawaguchi', 2015, 23, 201),
('Tales from the cafe', 'Toshikazu', 'Kawaguchi', 2017, 32, 221),
('Before your memory fades', 'Toshikazu', 'Kawaguchi', 2020, 12, 223),
('Be more Japan', 'DK', 'Travel', 2021, 15, 340),
('Paradise Crime Thrillers - Vol 01 - Wired in', 'Toby', 'Neal', 2012, 8, 351),
('Paradise Crime Thrillers - Vol 02 - Wired rogue', 'Toby', 'Neal', 2013, 22, 323),
('Paradise Crime Thrillers - Vol 03 - Wired hard', 'Toby', 'Neal', 2014, 2, 346),
('Paradise Crime Thrillers - Vol 04 - Wired dark', 'Toby', 'Neal', 2016, 15, 371),
('Paradise Crime Thrillers - Vol 05 - Wired dawn', 'Toby', 'Neal', 2018, 1, 301),
('Paradise Crime Thrillers - Vol 06 - Wired justice', 'Toby', 'Neal', 2019, 8, 324),
('Paradise Crime Thrillers - Vol 07 - Wired secret', 'Toby', 'Neal', 2020, 5, 359),
('Paradise Crime Thrillers - Vol 08 - Wired fear', 'Toby', 'Neal', 2021, 3, 341),
('Paradise Crime Thrillers - Vol 09 - Wired courage', 'Toby', 'Neal', 2023, 10, 369),
('Doppelganger', 'Naomi', 'Klein', 2025, 42, 427),
('Osamu Dazai Best Short Stories', 'Osamu', 'Dazai', 2011, 11, 167),
('Maid', 'Stephanie', 'Land', 2018, 15, 437),
('Love Marriage', 'Monica', 'Ali', 2023, 42, 428),
('The Vagabonds Way', 'Rolf', 'Potts', 2023, 4, 390),
('The Queens Gambit', 'Walter', 'Travis', 1984, 8, 439),
('Just like you', 'Nick', 'Hornby', 2019, 5, 277),
('The secret life of bees', 'Sue', 'Monk Kidd', 2022, 11, 429),
('The Bookshop Woman', 'Nanoko', 'Hanada', 2021, 3, 274),
('Intermezzo', 'Sally', 'Rooney', 2025, 12, 391),
('Mr Salary', 'Sally', 'Rooney', 2021, 2, 173),
('What I loved', 'Siri', 'Hustvedt', 2005, 3, 428),
('The summer without men', 'Siri', 'Hustvedt', 2008, 9, 451),
('Convenience Store Woman', ' Sayaka', 'Murata', 2022, 6, 210),
('The way of zen', ' Alan', 'Watts', 2008, 5, 254),
('Drinking Coffee elsewhere', 'Zz', 'Packer', 2013, 9, 302),
('Antarctica', 'Claire', 'Keagan', 2019, 3, 183),
('Forster', 'Claire', 'Keagan', 2016, 19, 83),
('The girls are good', 'Illaria', 'Bernardini', 2003, 7, 418),
('One of Them', 'Musa', 'Okwonga', 2019, 11, 402),
('Hello World', 'Hannah', 'Fry', 2021, 6, 426),
('Tomorrow, tomorrow, and tomorrow', 'Gabrielle', 'Zevin', 2023, 439),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343),
('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
('fake_book', 'Freida', 'Harris', 2001, 287, 428),
('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');

INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);

-- QUERIES --

SELECT * FROM books;

SELECT 
    CONCAT(SUBSTRING(title, 1, 10), '...') AS "short title"
FROM
    books;
    
SELECT REPLACE(title, ' ', '-') FROM books;

SELECT * FROM books;

SELECT * FROM books
WHERE author_fname LIKE '_a_'; 

SELECT
    CONCAT(
        'MY FAVORITE AUTHOR IS ',
        UPPER(author_fname),
        ' ',
        UPPER(author_lname),
        '!'
    ) AS yell
FROM books ORDER BY author_lname;

SELECT 
    CONCAT(title, ' - ', released_year) AS summary 
FROM books ORDER BY released_year DESC LIMIT 3;

SELECT 
    author_lname, COUNT(*) AS books_written
FROM
    books
GROUP BY author_lname
ORDER BY books_written DESC;

SELECT 
	author_lname, 
	COUNT(*) as books_written, 
	MAX(released_year) AS latest_release,
	MIN(released_year)  AS earliest_release,
      MAX(pages) AS longest_page_count
FROM books GROUP BY author_lname;

SELECT 
	author_lname, 
        author_fname,
	COUNT(*) as books_written, 
	MAX(released_year) AS latest_release,
	MIN(released_year)  AS earliest_release
FROM books GROUP BY author_lname, author_fname;

SELECT CONCAT(author_fname, ' ', author_lname) AS author, pages FROM books
WHERE pages = (SELECT MAX(pages) FROM books);

SELECT AVG(released_year) 
FROM books GROUP BY author_lname, author_fname;

SELECT 
    released_year AS year,
    COUNT(*) AS "# books",
    AVG(pages) AS "avg pages"
FROM books
GROUP BY released_year
ORDER BY released_year;

SELECT 
    title,
    stock_quantity,
    CASE
        WHEN stock_quantity <= 40 THEN '*'
        WHEN stock_quantity <= 70 THEN '**'
        WHEN stock_quantity <= 100 THEN '***'
        WHEN stock_quantity <= 140 THEN '****'
        ELSE '*****'
    END AS stock
FROM
    books;
    
SELECT title, released_year,
CASE
	WHEN released_year >= 2000 THEN 'modern lit'
    ELSE '20th century lit' 
END AS genre
FROM books;
