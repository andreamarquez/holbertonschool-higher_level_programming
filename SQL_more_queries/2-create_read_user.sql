-- This command creates the database hbtn_0d_2 if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- This command creates the MySQL server user user_0d_2 with the password user_0d_2_pwd if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- This command grants SELECT privilege to the user user_0d_2 on the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
