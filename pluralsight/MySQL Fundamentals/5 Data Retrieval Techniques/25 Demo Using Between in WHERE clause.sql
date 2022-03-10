-- WHERE clause Comparison Operators
-- IN
SELECT *
FROM sakila.actor
WHERE first_name IN ('NICK', 'JOHNNY', 'JOE', 'VIVIEN');

SELECT *
FROM sakila.actor
WHERE actor_id IN (1, 2, 3, 4, 5, 6, 7);

-- NOT IN
SELECT *
FROM sakila.actor
WHERE actor_id NOT IN (1, 2, 3, 4, 5, 6, 7);

-- In Subquery
SELECT *
FROM sakila.actor
WHERE first_name IN ('NICK', 'JOHNNY', 'JOE', 'VIVIEN')
    OR actor_id IN
        (SELECT actor_id FROM sakila.actor WHERE last_name='DEGENERES');

-- BETWEEN
SELECT *
FROM sakila.actor
WHERE actor_id>10 AND actor_id<20;

SELECT *
FROM sakila.actor
WHERE actor_id BETWEEN 10 AND 20;

SELECT *
FROM sakila.actor
WHERE actor_id NOT BETWEEN 10 AND 20;