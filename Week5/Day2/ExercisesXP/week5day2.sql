-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE items (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, price SMALLINT NOT NULL);
-- CREATE TABLE customers (id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL);
-- INSERT INTO items (name, price) VALUES ('small desk', 100), ('large desk', 300), ('fan', 80);
-- INSERT INTO customers (first_name, last_name) VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), 
-- ('Trevor', 'Green'),('Melanie', 'Johnson');

SELECT * FROM items WHERE price>80;
SELECT * FROM items WHERE price>=300;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE NOT (first_name = 'Scott');



