-- Retrieve the data with filter condition

SELECT *
FROM sakila.actor;

SELECT *
FROM sakila.actor
WHERE actor_id > 100;

SELECT *
FROM sakila.actor
WHERE actor_id < 100;

SELECT actor_id, first_name, last_name
FROM sakila.actor
WHERE first_name = 'Nick';