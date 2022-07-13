USE sakila;

-- Retrieve all columns of the table film where length is less than 80 min

SELECT *
FROM sakila.film
WHERE length < 80;

EXPLAIN SELECT *
FROM sakila.film
WHERE length < 80;

ALTER TABLE sakila.film 
ADD KEY IX_length (length);


-- 返回的行数达到一定比例，查询优化器跳过index，使用全表扫描
EXPLAIN SELECT *
FROM sakila.film
WHERE length < 100;

-- 分成2条分别执行，各自都会使用index提升性能
EXPLAIN SELECT *
FROM sakila.film
WHERE length < 61;

EXPLAIN SELECT *
FROM sakila.film
WHERE length >= 61 AND length <= 100;
-- 或
EXPLAIN SELECT *
FROM sakila.film
WHERE length BETWEEN 61 AND 100;

ALTER TABLE sakila.film 
DROP KEY IX_length;














