USE sakila;

-- Optimize Group By

SELECT title, length, COUNT(*)
FROM film
WHERE length < 100
GROUP BY title, length;

SELECT title, length, COUNT(*)
FROM film
WHERE length < 100
GROUP BY film_id;

EXPLAIN SELECT title, length, COUNT(*)
FROM film
WHERE length < 100
GROUP BY title, length;

EXPLAIN SELECT title, length, COUNT(*)
FROM film
WHERE length < 100
GROUP BY film_id;

-- Loop Test

CREATE TABLE `sakila`.`TestTable`
(title VARCHAR(100), length INT, count INT);

delimiter //
CREATE PROCEDURE FirstOption(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`TestTable`
		(`title`,
		`length`,
		`count`)
		SELECT title, length, COUNT(*)
		FROM film
		WHERE length < 100
		GROUP BY title, length;
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;


delimiter //
CREATE PROCEDURE SecondOption(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 - 1;
    IF p1 > 0 THEN		
		INSERT INTO `sakila`.`TestTable`
		(`title`,
		`length`,
		`count`)
		SELECT title, length, COUNT(*)
		FROM film
		WHERE length < 100
		GROUP BY film_id;
      ITERATE label1;
    END IF;
    LEAVE label1;
  END LOOP label1;
END//
delimiter ;

-- Execution Test

CALL FirstOption(1000);
TRUNCATE TABLE `sakila`.`TestTable`;
CALL SecondOption(1000);

-- Clean up
DROP PROCEDURE FirstOption;
DROP PROCEDURE SecondOption;

DROP TABLE `sakila`.`TestTable`;














