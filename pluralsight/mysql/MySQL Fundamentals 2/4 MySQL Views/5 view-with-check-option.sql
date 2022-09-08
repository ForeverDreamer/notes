USE sakila;
-- DML Operation Over View

SELECT language_id, name, last_update
FROM language;

CREATE VIEW DMLOperation
AS
SELECT language_id, name, last_update
FROM language
WHERE last_update = '2006-02-15 13:02:19'
WITH CHECK OPTION;

SELECT *
FROM DMLOperation;

-- Insert [HY000][1369] CHECK OPTION failed 'sakila.dmloperation'，last_update跟DMLOperation不一致
INSERT INTO DMLOperation 
		(name, last_update)
VALUES ('Hindi', '2013-02-15 13:02:19');

-- Insert 成功
INSERT INTO DMLOperation 
		(name, last_update)
VALUES ('Hindi', '2006-02-15 13:02:19');

SELECT *
FROM DMLOperation;

SELECT *
FROM language;

-- Update [HY000][1369] CHECK OPTION failed 'sakila.dmloperation'
UPDATE DMLOperation
SET last_update = '2013-02-15 13:02:19'
WHERE name = 'Hindi';

SELECT *
FROM DMLOperation;

-- [HY000][1369] CHECK OPTION failed 'sakila.dmloperation'
UPDATE DMLOperation
SET name = 'Spanish'
WHERE name = 'Hindi';

SELECT *
FROM DMLOperation;

-- WITH CHECK OPTION不检查Delete，成功
DELETE
FROM DMLOperation
WHERE name = 'Hindi';

SELECT *
FROM DMLOperation;

-- 不检查 Base Table DML
-- Insert 
INSERT INTO language 
		(name, last_update)
VALUES ('New Lang', '2006-02-15 13:02:19');

SELECT language_id, name, last_update
FROM language;

UPDATE language
SET last_update = '2022-02-15 13:02:19'
WHERE name = 'German';

# 视图里查不到German
SELECT language_id, name, last_update
FROM DMLOperation;

# Base Table查得到German
SELECT language_id, name, last_update
FROM language;

-- 
DROP VIEW DMLOperation;











