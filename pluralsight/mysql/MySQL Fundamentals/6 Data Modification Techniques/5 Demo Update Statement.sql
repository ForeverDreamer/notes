-- UPDATE Statement
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

-- Update Single Row Single Column
UPDATE actor_sample
SET first_name='Pinal'
WHERE actor_id=1;

UPDATE actor_sample
SET last_name='Dave'
WHERE actor_id=1;

SELECT *
FROM actor_sample
WHERE actor_id=1;

-- Update Single Row Multiple Columns
UPDATE actor_sample
SET first_name='Pinal', last_name='Dave'
WHERE actor_id=2;

SELECT *
FROM actor_sample
WHERE actor_id=2;

-- Update Multiple Rows Single Column
UPDATE actor_sample
SET first_name='Pinal'
WHERE actor_id IN (3, 4, 5);

SELECT *
FROM actor_sample
WHERE actor_id IN (3, 4, 5);

-- Update Multiple Rows Multiple Columns
UPDATE actor_sample
SET first_name='Pinal', last_name='Dave', last_update=DEFAULT
WHERE actor_id IN (6, 7, 8);

SELECT *
FROM actor_sample
WHERE actor_id IN (6, 7, 8);

-- Update using SELECT Statement
UPDATE actor_sample
SET first_name='Nupur'
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id=1);

SELECT *
FROM actor_sample
WHERE actor_id=1;

-- Clean up
DROP TABLE actor_sample