-- LIKE
SELECT *
FROM sakila.actor
WHERE first_name LIKE 'A%';

SELECT *
FROM sakila.actor
WHERE first_name LIKE 'AL%';

SELECT *
FROM sakila.actor
WHERE first_name LIKE 'A__E';

SELECT *
FROM sakila.actor
WHERE first_name LIKE 'A__E%';

SELECT *
FROM sakila.actor
WHERE first_name LIKE 'A%E%';

SELECT *
FROM sakila.actor
WHERE first_name LIKE 'A%E%' AND last_name LIKE 'W%';

-- NULL
SELECT *
FROM sakila.address;

SELECT *
FROM sakila.address
WHERE address2 IS NULL;

SELECT *
FROM sakila.address
WHERE address2 IS NOT NULL;