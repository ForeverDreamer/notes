-- Retrieve selected columns from table

SELECT *
FROM sakila.actor;

SELECT first_name, last_name
FROM sakila.actor;

SELECT first_name, last_name
FROM sakila.actor
ORDER BY last_name DESC;