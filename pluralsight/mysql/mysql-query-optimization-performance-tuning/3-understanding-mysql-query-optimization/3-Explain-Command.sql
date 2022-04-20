USE sakila;

EXPLAIN SELECT *
FROM actor;

EXPLAIN SELECT *
FROM actor
CROSS JOIN address;

EXPLAIN SELECT *
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id;

SELECT *
FROM actor
CROSS JOIN address
UNION 
SELECT *
FROM actor
CROSS JOIN address
UNION 
SELECT *
FROM actor
CROSS JOIN address
UNION 
SELECT *
FROM actor
CROSS JOIN address
UNION 
SELECT *
FROM actor
CROSS JOIN address
UNION 
SELECT *
FROM actor
CROSS JOIN address;
