-- Create the database
CREATE DATABASE world;

-- Connect to the newly created database
USE world;

-- Create the 'capital' table
CREATE TABLE capital (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(45) NOT NULL,
    capital VARCHAR(45) NOT NULL
);

-- Create the 'flags' table
CREATE TABLE flags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(45) NOT NULL,
    flag TEXT
);

-- Select data from the tables
SELECT * FROM flags;
SELECT * FROM capital;

CREATE TABLE visited_countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_code CHAR(2) NOT NULL UNIQUE
);

INSERT INTO visited_countries (country_code) VALUES
('FR'),  -- France
('US'),  -- USA
('ZA');  -- South Africa

Select * From visited_countries;

Create Table world_food (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country Varchar(45) not null,
    rice_production float,
    wheat_production float
    );

INSERT INTO world_food (country, rice_production, wheat_production)
VALUES
('Australia', 0.42, 31.9),
('Brazil', 13.98, 7.9),
('China', 212.84, 136.9),
('Ethiopia', 0.2, 5.2),
('India', 195.43, 109.6),
('Iran', 1.6, 10.1),
('Pakistan', 13.98, 27.5),
('Ukraine', 0.05, 32.2),
('United States', 8.7, 44.8),
('Italy', 1.45, 7.3);

Select * From world_food;

	

