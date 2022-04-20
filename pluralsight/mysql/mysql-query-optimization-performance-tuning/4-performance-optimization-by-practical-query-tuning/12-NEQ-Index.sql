USE sakila;

SELECT *
FROM customer
WHERE store_id <> 2;

EXPLAIN SELECT *
FROM customer
WHERE store_id <> 2;

SELECT DISTINCT store_id 
FROM customer;

SELECT *
FROM customer
WHERE store_id = 1;

EXPLAIN SELECT *
FROM customer
WHERE store_id = 1;













