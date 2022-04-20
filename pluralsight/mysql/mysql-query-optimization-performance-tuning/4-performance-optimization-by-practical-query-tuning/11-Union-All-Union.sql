USE sakila;

-- Union vs Union all

SELECT staff_id, first_name, last_name
FROM staff s
UNION ALL
SELECT customer_id, first_name, last_name
FROM customer c
UNION ALL
SELECT actor_id, first_name, last_name
FROM actor a;

SELECT staff_id, first_name, last_name
FROM staff s
UNION
SELECT customer_id, first_name, last_name
FROM customer c
UNION
SELECT actor_id, first_name, last_name
FROM actor a;

-- Explain

EXPLAIN SELECT staff_id, first_name, last_name
FROM staff s
UNION ALL
SELECT customer_id, first_name, last_name
FROM customer c
UNION ALL
SELECT actor_id, first_name, last_name
FROM actor a;

EXPLAIN SELECT staff_id, first_name, last_name
FROM staff s
UNION
SELECT customer_id, first_name, last_name
FROM customer c
UNION
SELECT actor_id, first_name, last_name
FROM actor a;

-- 


-- Loop Test
CREATE TABLE `sakila`.`customertest`
(id INT, first_name VARCHAR(100), last_name VARCHAR(100));

delimiter //
CREATE PROCEDURE UnionAllOption(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`customertest` (id, first_name, last_name)
		SELECT staff_id, first_name, last_name
		FROM staff s
		UNION ALL
		SELECT customer_id, first_name, last_name
		FROM customer c
		UNION ALL
		SELECT actor_id, first_name, last_name
		FROM actor a;
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;


delimiter //
CREATE PROCEDURE UnionOption(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN
		INSERT INTO `sakila`.`customertest` (id, first_name, last_name)			
		SELECT staff_id, first_name, last_name
		FROM staff s
		UNION
		SELECT customer_id, first_name, last_name
		FROM customer c
		UNION
		SELECT actor_id, first_name, last_name
		FROM actor a;
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;

-- Execution Test

CALL UnionAllOption(1000);
TRUNCATE TABLE `sakila`.`customertest`;
CALL UnionOption(1000);

-- Clean up
DROP PROCEDURE UnionAllOption;
DROP PROCEDURE UnionOption;

DROP TABLE `sakila`.`customertest`;

