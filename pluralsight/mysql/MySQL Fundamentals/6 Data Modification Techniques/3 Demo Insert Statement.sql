-- INSERT Statement
USE sakila;

CREATE TABLE actor_sample(
    actor_id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    first_name varchar(45) NOT NULL,
    last_name varchar(45) NULL,
    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (actor_id)
);

-- Insert Single Row
INSERT INTO actor_sample(first_name, last_name, last_update)
VALUES('Pinal', 'Dave', '2013-04-15');

-- Check Data
SELECT *
FROM actor_sample;

-- Insert Single Row
INSERT INTO actor_sample(first_name, last_name)
VALUES('Tom', 'Cruise');

-- Check Data
SELECT *
FROM actor_sample;

-- Insert Single Row
INSERT INTO actor_sample(first_name)
VALUES('Jack');

-- Check Data
SELECT *
FROM actor_sample;

-- Insert Single Row
INSERT INTO actor_sample(first_name, last_name, last_update)
VALUES('John', NULL, DEFAULT);

-- Check Data
SELECT *
FROM actor_sample;

-- Insert Multiple Values
INSERT INTO sakila.actor_sample(first_name, last_name, last_update)
VALUES ('Pinal', 'Dave', '2013-04-17'),
       ('Nupur', 'Dave', '2013-04-18'),
       ('Shaivi', 'Dave', '2013-04-19');

SELECT *
FROM actor_sample;

-- Subquery
INSERT INTO actor_sample(first_name, last_name, last_update)
    SELECT first_name, last_name, last_update
    FROM actor
    WHERE first_name='NICK';

SELECT *
FROM actor_sample;

-- Clean up
DROP TABLE actor_sample