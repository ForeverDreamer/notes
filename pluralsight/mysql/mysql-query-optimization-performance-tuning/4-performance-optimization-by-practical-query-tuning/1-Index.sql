-- Location of Sakila Database - https://dev.mysql.com/downloads/

USE sakila;

-- Retrieve film_id and length of the film where length is less than 50 mins and 100 mins

SELECT *
FROM film;

SELECT *
FROM sakila.film
WHERE length < 50;

EXPLAIN SELECT *
FROM sakila.film
WHERE length < 50;

ALTER TABLE sakila.film 
ADD KEY IX_length (length);

EXPLAIN SELECT *
FROM sakila.film
WHERE length < 50;

EXPLAIN SELECT *
FROM sakila.film
WHERE length < 100;

EXPLAIN SELECT film_id, length
FROM sakila.film
WHERE length < 100;

ALTER TABLE sakila.film 
DROP KEY IX_length;














