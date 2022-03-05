-- Retrieve the data with filter condition and ordered by columns

SELECT *
FROM sakila.actor
WHERE first_name = 'Nick';

SELECT actor_id, first_name, last_name
FROM sakila.actor
WHERE first_name = 'Nick'
ORDER BY actor_id DESC;

SELECT actor_id, first_name, last_name
FROM sakila.actor
WHERE actor_id > 100
ORDER BY first_name DESC , last_name DESC;