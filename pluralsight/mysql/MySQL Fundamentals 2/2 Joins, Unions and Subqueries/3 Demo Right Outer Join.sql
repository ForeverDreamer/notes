use sakila;
-- Create table 1
CREATE TABLE table1(
    ID INT,
    Value VARCHAR(10)
);

INSERT INTO table1(ID, Value)
SELECT 1, 'First'
UNION ALL
SELECT 2, 'Second'
UNION ALL
SELECT 3, 'Third'
UNION ALL
SELECT 4, 'Fourth'
UNION ALL
SELECT 5, 'Fifth';

-- Create table 2
CREATE TABLE table2(
    ID INT,
    Value VARCHAR(10)
);

INSERT INTO table2(ID, Value)
SELECT 1, 'First'
UNION ALL
SELECT 2, 'Second'
UNION ALL
SELECT 3, 'Third'
UNION ALL
SELECT 6, 'Sixth'
UNION ALL
SELECT 7, 'Seventh'
UNION ALL
SELECT 8, 'Eighth';

SELECT *
FROM table1;

SELECT *
FROM table2;

/* RIGHT [OUTER] JOIN */
SELECT t1.ID AS T1ID, t1.Value AS T1Value,
       t2.ID AS T2ID, t2.Value AS T2Value
FROM table1 t1
RIGHT JOIN table2 t2 on t1.ID=t2.ID;

SELECT t2.ID AS ID, t1.Value AS T1Value, t2.Value AS T2Value
FROM table1 t1
RIGHT JOIN table2 t2 on t1.ID=t2.ID;

DROP TABLE IF EXISTS table1, table2;