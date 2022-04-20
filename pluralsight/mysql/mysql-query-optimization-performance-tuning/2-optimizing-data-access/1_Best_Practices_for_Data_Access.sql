USE sakila;

-- Regular select statement
SELECT * 
FROM actor;

-- Use WHERE clause 
SELECT *
FROM actor
WHERE first_name LIKE 'A%';

-- List  clause 
SELECT actor_id, first_name, Last_name
FROM actor
WHERE first_name LIKE 'A%';

-- Order By clause
SELECT actor_id, first_name, Last_name
FROM actor
WHERE first_name LIKE 'A%'
ORDER BY Last_name;













-- ----------------------------------
-- ----------------------------------
-- Why Star is NOT good idea
SELECT *
FROM customer;

SELECT *
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id;

SELECT *
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN store ON store.store_id = customer.store_id;

SELECT *
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN store ON store.store_id = customer.store_id
INNER JOIN staff ON staff.staff_id = rental.staff_id;

SELECT customer.*, 
staff.first_name AS Staff_First_Name, staff.last_name AS Staff_Last_Name
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN store ON store.store_id = customer.store_id
INNER JOIN staff ON staff.staff_id = rental.staff_id;

SELECT customer.first_name, customer.last_name, 
staff.first_name AS Staff_First_Name, staff.last_name AS Staff_Last_Name
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN store ON store.store_id = customer.store_id
INNER JOIN staff ON staff.staff_id = rental.staff_id;

SELECT DISTINCT customer.first_name, customer.last_name,
staff.first_name AS Staff_First_Name, staff.last_name AS Staff_Last_Name
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN store ON store.store_id = customer.store_id
INNER JOIN staff ON staff.staff_id = rental.staff_id;






















