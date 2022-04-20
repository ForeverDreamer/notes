USE sakila;

EXPLAIN EXTENDED SELECT *
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id;

SHOW WARNINGS;