-- This command creates the MySQL server user user_0d_1 with the password user_0d_1_pwd if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- This command sets the password for user_0d_1 to user_0d_1_pwd
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- This command grants all privileges to the user user_0d_1 on localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';