-- Retrieve results based on function

SELECT *
FROM sakila.actor;

SELECT *
FROM sakila.payment;

-- Integer Operations

SELECT amount,
       ROUND(amount) Amnt, ROUND(amount,1) Amnt1,
       FLOOR(amount) FloorAmnt, CEILING(amount) CeilingAmnt
FROM sakila.payment;