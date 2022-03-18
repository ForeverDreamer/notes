use sakila;

CREATE TABLE students(
    student_id INT,
    student_name VARCHAR(10)
);

INSERT INTO students(student_id, student_name)
SELECT 1, 'John'
UNION ALL
SELECT 2, 'Matt'
UNION ALL
SELECT 3, 'James';

CREATE TABLE classes(
    class_id INT,
    class_name VARCHAR(10)
);

INSERT INTO classes(class_id, class_name)
SELECT 1, 'Maths'
UNION ALL
SELECT 2, 'Arts'
UNION ALL
SELECT 3, 'History';

CREATE TABLE student_class(
    student_id INT,
    class_id INT
);

INSERT INTO student_class(student_id, class_id)
SELECT 1, 1
UNION ALL
SELECT 1, 2
UNION ALL
SELECT 3, 1
UNION ALL
SELECT 3, 2
UNION ALL
SELECT 3, 3;