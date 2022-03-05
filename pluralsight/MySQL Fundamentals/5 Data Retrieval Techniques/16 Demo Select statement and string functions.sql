-- String Operations

-- Concat
SELECT CONCAT(first_name, ' ', last_name) AS FullName
FROM sakila.actor;

-- LEFT function
SELECT CONCAT(first_name, ' ', last_name) AS FullName,
       CONCAT(LEFT(first_name,1), LEFT(last_name,1)) AS FirstInitial
FROM sakila.actor;

-- LENGTH function
SELECT FullName, LENGTH(FullName) AS Length
FROM (
    SELECT CONCAT(first_name, ' ', last_name) AS FullName
    FROM sakila.actor
) AS FullNameTable;

-- Various function
SELECT FullName, REVERSE(FullName) AS ReverseFullName, REPLACE(FullName, 'S', '_') AS ReplaceExample
FROM (
    SELECT CONCAT(first_name, ' ', last_name) AS FullName
    FROM sakila.actor
) AS FullNameTable;