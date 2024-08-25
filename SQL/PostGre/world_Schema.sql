-- Create the database
CREATE DATABASE world;

-- Connect to the newly created database
\c world;

-- Create the 'capital' table
CREATE TABLE capital (
    id SERIAL PRIMARY KEY,
    country VARCHAR(45),
    capital VARCHAR(45)
);

-- Create the 'flags' table
CREATE TABLE flags (
    id SERIAL PRIMARY KEY,
    country VARCHAR(45),
    flag Text
);
