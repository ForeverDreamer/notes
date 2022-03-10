-- DELETE Statement
USE sakila;

-- Populate Sample Table
CREATE TABLE actor_sample(
    actor_id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    first_name varchar(45) NOT NULL,
    last_name varchar(45) NULL,
    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (actor_id)
);

INSERT INTO actor_sample(first_name, last_name, last_update)
SELECT first_name, last_name, last_update
FROM actor;

-- Delete Single Row
DELETE
FROM actor_sample
WHERE actor_id=1;

SELECT *
FROM actor_sample;

-- Delete Multiple Rows
DELETE
FROM actor_sample
WHERE actor_id IN (3, 4, 5);

SELECT *
FROM actor_sample;

-- Delete using SELECT Statement
DELETE
FROM actor_sample
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id=1);

SELECT *
FROM actor_sample
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id=1);

-- Delete all Rows from Table
DELETE
FROM actor_sample;

SELECT *
FROM actor_sample;

-- Clean up
DROP TABLE actor_sample