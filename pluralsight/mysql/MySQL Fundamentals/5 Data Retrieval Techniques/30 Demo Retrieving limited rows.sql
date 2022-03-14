-- Limit Keyword
SELECT *
FROM sakila.actor
ORDER BY actor_id;

SELECT *
FROM sakila.actor
ORDER BY actor_id
LIMIT 10;

-- skip 15, limit 10
SELECT *
FROM sakila.actor
ORDER BY actor_id
LIMIT 15, 10;