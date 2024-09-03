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
