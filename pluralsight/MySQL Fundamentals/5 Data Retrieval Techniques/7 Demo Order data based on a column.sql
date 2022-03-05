-- Retrieve all the data ordered by single column

SELECT *
FROM sakila.actor;

SELECT *
FROM sakila.actor
ORDER BY first_name;

SELECT *
FROM sakila.actor
ORDER BY last_name;

SELECT *
FROM sakila.actor
ORDER BY first_name DESC;

SELECT *
FROM sakila.actor
ORDER BY last_name DESC;