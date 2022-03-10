-- ORDER BY clause
SELECT *
FROM sakila.address
ORDER BY district;

SELECT *
FROM sakila.address
ORDER BY district DESC;

SELECT *
FROM sakila.address
ORDER BY district, postal_code DESC;

SELECT actor_id, CONCAT(first_name, ' ', last_name) AS FullName
FROM sakila.actor
ORDER BY CONCAT(first_name, ' ', last_name);

SELECT actor_id, CONCAT(first_name, ' ', last_name) AS FullName
FROM sakila.actor
ORDER BY FullName;

-- 按第2个column，即actor_id排序
SELECT actor_id, CONCAT(first_name, ' ', last_name) AS FullName
FROM sakila.actor
ORDER BY 1;

-- 按第2个column，即FullName排序
SELECT actor_id, CONCAT(first_name, ' ', last_name) AS FullName
FROM sakila.actor
ORDER BY 2;