USE sakila;

-- Retrieve row number 396 to 400 from table customer where table is ordered by customer_id

SELECT *
FROM customer;

SELECT *
FROM customer
LIMIT 400;

SELECT *
FROM customer
ORDER BY customer_id
LIMIT 400;

SELECT *
FROM customer
ORDER BY customer_id
LIMIT 395,5;





















