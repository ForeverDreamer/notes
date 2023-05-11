USE sakila;

-- Displaying Index
SHOW INDEX FROM film FROM sakila;
SHOW INDEX FROM film;

SELECT *
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_NAME = 'film';

-- Creating Index
CREATE INDEX idx_film_length ON film (length);

-- Query using Index
SELECT film_id, length
FROM film
WHERE length = 100;

-- Explain Index Usage
EXPLAIN SELECT film_id, length
FROM film
WHERE length = 100;

-- Droping Index
DROP Index idx_film_length ON film;


EXPLAIN SELECT first_name, last_name, SUM(amount) AS total
FROM staff INNER JOIN payment
  ON staff.staff_id = payment.staff_id
     AND
     payment.payment_date LIKE '2005-08%'
GROUP BY first_name, last_name;

SELECT CONNECTION_ID();
EXPLAIN FOR CONNECTION 9;

SHOW CHARACTER SET;

SELECT count(*) FROM payment WHERE  payment.payment_date LIKE '2005-08%';
SELECT count(*) FROM payment WHERE staff_id=2;
SELECT * FROM INFORMATION_SCHEMA.SCHEMATA;
SHOW ENGINE INNODB STATUS;
SELECT NAME, COMMENT FROM INFORMATION_SCHEMA.INNODB_METRICS WHERE NAME LIKE '%ibuf%';
SELECT (SELECT COUNT(*) FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE
       WHERE PAGE_TYPE LIKE 'IBUF%') AS change_buffer_pages,
       (SELECT COUNT(*) FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE) AS total_pages,
       (SELECT ((change_buffer_pages/total_pages)*100))
       AS change_buffer_page_percentage;



EXPLAIN ANALYZE
SELECT first_name, last_name, SUM(amount) AS total
FROM staff INNER JOIN payment
  ON staff.staff_id = payment.staff_id
     AND
     payment.payment_date LIKE '2005-08%'
GROUP BY first_name, last_name;

















