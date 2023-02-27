-- A locking read clause in an outer statement does not lock the rows of a table in a nested subquery
-- unless a locking read clause is also specified in the subquery
-- 初始化数据
USE examples;
CREATE TABLE t1 (
    i INT,
    PRIMARY KEY (i)
) ENGINE = InnoDB;
CREATE TABLE t2 (
    i INT,
    PRIMARY KEY (i)
) ENGINE = InnoDB;
SHOW TABLES;

INSERT INTO t1 (i) VALUES(1),(2),(3);
INSERT INTO t2 (i) VALUES(1),(2),(3);

SELECT * from  t1;
SELECT * from  t2;

-- Session 1
START TRANSACTION;
SELECT * FROM t1 WHERE i IN (SELECT i FROM t2) FOR UPDATE;
SELECT * FROM t1 WHERE i IN (SELECT i FROM t2 FOR UPDATE) FOR UPDATE;
COMMIT;

-- Session 2
START TRANSACTION;
SELECT * FROM t2 FOR UPDATE;
ROLLBACK;

DROP TABLE IF EXISTS t1, t2;


-- Locking Read Examples
CREATE TABLE parent (
     id INT NOT NULL PRIMARY KEY,
     name VARCHAR(50),
     INDEX name_idx (name)
) ENGINE = InnoDB;

CREATE TABLE child (
     id INT NOT NULL PRIMARY KEY,
     parent_id INT,
     INDEX parent_idx (parent_id),
     name VARCHAR(50),
     INDEX name_idx (name),
     FOREIGN KEY (parent_id)
        REFERENCES parent(id)
            ON DELETE CASCADE
) ENGINE = InnoDB;

INSERT INTO parent (id, name) VALUES(1, 'Jones');

-- Session 1
START TRANSACTION;
SELECT * FROM parent WHERE NAME = 'Jones' FOR SHARE;
INSERT INTO child (id, parent_id, name) VALUES(1, 1, 'Sandy');
COMMIT;

-- Session 2
START TRANSACTION;
SELECT * FROM parent WHERE NAME = 'Jones' FOR UPDATE;
COMMIT;

DROP TABLE IF EXISTS parent, child;


-- Locking Read Concurrency with NOWAIT and SKIP LOCKED
-- Session 1
CREATE TABLE t (
    i INT,
    PRIMARY KEY (i)
) ENGINE = InnoDB;
INSERT INTO t (i) VALUES(1),(2),(3);

START TRANSACTION;
SELECT * FROM t WHERE i = 2 FOR UPDATE;

-- Session 2
START TRANSACTION;
SELECT * FROM t WHERE i = 2 FOR UPDATE NOWAIT;

-- Session 3
START TRANSACTION;
SELECT * FROM t FOR UPDATE SKIP LOCKED;

DROP TABLE IF EXISTS t;