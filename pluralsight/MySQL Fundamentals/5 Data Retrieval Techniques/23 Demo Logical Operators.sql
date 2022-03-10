-- WHERE clause Comparison Operators
SELECT *
FROM sakila.actor
WHERE first_name='KENNETH';

-- AND
SELECT *
FROM sakila.actor
WHERE first_name='KENNETH' AND actor_id < 100;

SELECT *
FROM sakila.actor
WHERE first_name='KENNETH' AND actor_id < 100 AND last_name='TORN';

-- OR
SELECT *
FROM sakila.actor
WHERE first_name='KENNETH' OR actor_id < 100;

SELECT *
FROM sakila.actor
WHERE first_name='KENNETH' OR actor_id < 100 OR last_name='TEMPLE';

-- NOT
SELECT *
FROM sakila.actor
WHERE NOT actor_id=5;

SELECT *
FROM sakila.actor
WHERE actor_id<>5;

-- All together
SELECT *
FROM sakila.actor
WHERE (first_name='KENNETH' AND actor_id<100) OR last_name='TEMPLE';

SELECT *
FROM sakila.actor
WHERE first_name='KENNETH' AND (actor_id<100 OR last_name='TEMPLE');
