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