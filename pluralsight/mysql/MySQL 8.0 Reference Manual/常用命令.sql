-- 登录

/*
mysql -uroot -p
my-secret-pw
*/

SHOW DATABASES;
DROP DATABASE IF EXISTS examples;

SHOW TABLES FROM examples;
DROP TABLE IF EXISTS examples.address;
DROP TABLE IF EXISTS examples.address, examples.some_table, examples.user_account;

SHOW TABLE STATUS FROM examples;
SELECT * FROM INFORMATION_SCHEMA.INNODB_TABLES WHERE NAME LIKE 'examples/%';

SELECT @@default_storage_engine;

SELECT @@innodb_file_per_table;

SELECT @@datadir, @@innodb_data_home_dir, @@innodb_directories;