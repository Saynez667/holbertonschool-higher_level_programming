-- This script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases of your MySQL server to the user user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Update the privileges of the MySQL user user_0d_1.	
FLUSH PRIVILEGES;
