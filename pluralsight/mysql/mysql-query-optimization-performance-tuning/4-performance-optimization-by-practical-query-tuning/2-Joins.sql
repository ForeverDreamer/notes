USE sakila;

-- When to use One Complex Query vs Many Simple Queries?

-- -----------------------------------------------------------------------
-- Example 1

SELECT *
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
INNER JOIN film_category fc ON fc.film_id = fa.film_id
WHERE f.film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM film
WHERE film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM film_actor
WHERE film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM film_category
WHERE film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

-- Complex Query = 10.799000
-- Multiple Queries = 2.399000 + 2.399000 +2.399000 = 7.197

-- -----------------------------------------------------------------------
-- Example 1

SELECT *
FROM film f
INNER JOIN inventory ia ON f.film_id = ia.film_id
INNER JOIN store st ON st.store_id = ia.store_id
INNER JOIN address ad ON ad.address_id = st.address_id
WHERE f.film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

-- Decomposing query
SELECT *
FROM film
WHERE film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM Inventory 
WHERE film_id = 10;
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM store 
WHERE store_id in (1,2);
SHOW STATUS LIKE 'Last_Query_Cost';

SELECT *
FROM address 
WHERE address_id in (1,2);
SHOW STATUS LIKE 'Last_Query_Cost';

-- Complex Query = 6.199000
-- Multiple Queries = 2.399000 + 2.399000 +2.399000 = 7.197 

























