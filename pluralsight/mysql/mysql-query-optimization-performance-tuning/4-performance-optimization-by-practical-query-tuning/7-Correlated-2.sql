USE sakila;

-- What is the most optimal way to write queries - Subquery vs Exists vs Joins?

SELECT *
FROM inventory i
WHERE i.film_id IN (
SELECT f.film_id
FROM film f
WHERE f.length < 55);

EXPLAIN SELECT *
FROM inventory i
WHERE i.film_id IN (
SELECT f.film_id
FROM film f
WHERE f.length < 55);

-- EXISTS

SELECT *
FROM inventory i
WHERE EXISTS (
SELECT f.film_id
FROM film f
WHERE f.length < 55
AND i.film_id = f.film_id);

EXPLAIN SELECT *
FROM inventory i
WHERE EXISTS (
SELECT f.film_id
FROM film f
WHERE f.length < 55
AND i.film_id = f.film_id);

-- JOIN

SELECT i.*
FROM inventory i
INNER JOIN film f ON i.film_id = f.film_id
WHERE f.length < 55;

EXPLAIN SELECT i.*
FROM inventory i
INNER JOIN film f ON i.film_id = f.film_id
WHERE f.length < 55;

-- Stored Procedures Performance test
CREATE TABLE `sakila`.`inventorycopy` (
  `inventory_id` mediumint(8),
  `film_id` smallint(5) NOT NULL,
  `store_id` tinyint(3) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);


delimiter //
CREATE PROCEDURE SubQ(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`inventorycopy`
		(`inventory_id`,
		`film_id`,
		`store_id`,
		`last_update`)
		SELECT *
		FROM inventory i
		WHERE i.film_id IN (
		SELECT f.film_id
		FROM film f
		WHERE f.length < 55);
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;

-- Loop to write
delimiter //
CREATE PROCEDURE ExistQ(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`inventorycopy`
		(`inventory_id`,
		`film_id`,
		`store_id`,
		`last_update`)
		SELECT *
		FROM inventory i
		WHERE EXISTS (
		SELECT f.film_id
		FROM film f
		WHERE f.length < 55
		AND i.film_id = f.film_id);
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;

-- Loop to write
delimiter //
CREATE PROCEDURE JoinQ(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`inventorycopy`
		(`inventory_id`,
		`film_id`,
		`store_id`,
		`last_update`)
		SELECT i.*
		FROM inventory i
		INNER JOIN film f ON i.film_id = f.film_id
		WHERE f.length < 55;
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;

-- Execution Test

CALL SubQ(1000);
TRUNCATE TABLE `sakila`.`filmcopy`;

CALL ExistQ(1000);
TRUNCATE TABLE `sakila`.`filmcopy`;

CALL JoinQ(1000);

-- Clean up
DROP PROCEDURE ExistQ;
DROP PROCEDURE SubQ;
DROP PROCEDURE JoinQ;
DROP TABLE `sakila`.`inventorycopy`;












