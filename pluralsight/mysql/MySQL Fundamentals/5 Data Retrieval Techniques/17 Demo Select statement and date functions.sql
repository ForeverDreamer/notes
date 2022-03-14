-- Date Operations
-- DATE_FORMAT function
SELECT CONCAT(first_name, ' ', last_name) AS FullName,
       DATE_FORMAT(last_update, '%m/%d/%y') AS LastUpdated1,
       DATE_FORMAT(last_update, '%d-%m-%Y') AS LastUpdated1,
       DATE_FORMAT(last_update, '%d %b %Y %T:%f') AS LastUpdated1
FROM sakila.actor;

SELECT CONCAT(first_name, ' ', last_name) AS FullName,
       DATE_FORMAT(last_update, GET_FORMAT(DATETIME, 'EUR')) AS LastUpdated1,
       DATE_FORMAT(last_update, GET_FORMAT(DATETIME, 'ISO')) AS LastUpdated2,
       DATE_FORMAT(last_update, GET_FORMAT(DATETIME, 'USA')) AS LastUpdated3
FROM sakila.actor;

SELECT CONCAT(first_name, ' ', last_name) AS FullName,
       DATE_FORMAT(last_update, GET_FORMAT(DATE, 'EUR')) AS LastUpdated1,
       DATE_FORMAT(last_update, GET_FORMAT(DATE, 'ISO')) AS LastUpdated2,
       DATE_FORMAT(last_update, GET_FORMAT(DATE, 'USA')) AS LastUpdated3
FROM sakila.actor;

-- other function
SELECT rental_date,
       DAYOFWEEK(rental_date) AS DayOfWeek,
       QUARTER(rental_date) AS Quarter,
       WEEK(rental_date) AS fWeek,
       MONTHNAME(rental_date) AS Monthname
FROM sakila.rental;