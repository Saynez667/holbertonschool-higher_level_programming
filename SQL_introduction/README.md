## SQL Introduction Project 🚀

This project introduces fundamental SQL concepts and their application using MySQL. It covers creating databases, tables, and manipulating data within them.

### Learning Objectives 🎯

By completing this project, you will be able to:

*   Understand what a database is 🗄️
*   Explain relational databases 🔗
*   Define what SQL stands for and its purpose 🗣️
*   Describe MySQL 🐬
*   Create databases and tables in MySQL 🛠️
*   Understand what DDL and DML stand for
*   CREATE or ALTER a table
*   SELECT data from a table
*   INSERT, UPDATE or DELETE data
*   Understand what are subqueries
*   How to use MySQL functions

### Requirements ⚙️

*   **Editors:** vi, vim, emacs
*   **Environment:** Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
*   All files must end with a newline character ↵
*   SQL queries must be commented 💬
*   Files should start with a comment describing the task ℹ️
*   SQL keywords should be in uppercase ⌨️
*   A `README.md` file is mandatory 📝

### Setup Instructions 💻

1.  **Update Package List:**

    ```
    sudo apt update
    ```
2.  **Install MySQL Server:**

    ```
    sudo apt install mysql-server
    ```
3.  **Check MySQL Version:**

    ```
    mysql --version
    ```
4.  **Start MySQL Service:**

    ```
    sudo service mysql start
    ```
5.  **Connect to MySQL:**

    ```
    sudo mysql -uroot
    ```

### Tasks 📚

1.  **List Databases**
    *   Write a script that lists all databases of your MySQL server.
    *   File: `0-list_databases.sql`
    ```
    -- Lists all databases of your MySQL server.
    SHOW DATABASES;
    ```
2.  **Create a Database**
    *   Write a script that creates the database `hbtn_0c_0` in your MySQL server.
    *   If the database `hbtn_0c_0` already exists, your script should not fail.
    *   You are not allowed to use the `SELECT` or `SHOW` statements.
    *   File: `1-create_database_if_missing.sql`
    ```
    -- Creates the database hbtn_0c_0.
    CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
    ```
3.  **Delete a Database**
    *   Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
    *   If the database `hbtn_0c_0` doesn’t exist, your script should not fail.
    *   You are not allowed to use the `SELECT` or `SHOW` statements.
    *   File: `2-remove_database.sql`
    ```
    -- Deletes the database hbtn_0c_0.
    DROP DATABASE IF EXISTS hbtn_0c_0;
    ```
4.  **List Tables**
    *   Write a script that lists all the tables of a database in your MySQL server. The database name will be passed as an argument of the mysql command (in the following example: mysql is the name of the database)
    *   File: `3-list_tables.sql`
    ```
    -- Lists all the tables of a database.
    SHOW TABLES;
    ```
5.  **First Table**
    *   Write a script that creates a table called `first_table` in the current database in your MySQL server.
        *   `first_table` description:
            *   `id` INT
            *   `name` VARCHAR(256)
    *   The database name will be passed as an argument of the mysql command.
    *   If the table `first_table` already exists, your script should not fail.
    *   You are not allowed to use the `SELECT` or `SHOW` statements.
    *   File: `4-first_table.sql`
    ```
    -- Creates a table called first_table.
    CREATE TABLE IF NOT EXISTS first_table (
        id INT,
        name VARCHAR(256)
    );
    ```
6.  **Full Description**
    *   Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    *   The database name will be passed as an argument of the mysql command.
    *   You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements.
    *   File: `5-full_table.sql`
    ```
    -- Prints the description of the table first_table.
    SHOW CREATE TABLE first_table;
    ```
7.  **List All in Table**
    *   Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    *   All fields should be printed.
    *   The database name will be passed as an argument of the mysql command.
    *   File: `6-list_values.sql`
    ```
    -- Lists all rows of the table first_table.
    SELECT * FROM first_table;
    ```
8.  **First Add**
    *   Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
    *   New row:
        *   `id` = 89
        *   `name` = Best School
    *   The database name will be passed as an argument of the mysql command.
    *   File: `7-insert_value.sql`
    ```
    -- Inserts a new row in the table first_table.
    INSERT INTO first_table (id, name) VALUES (89, 'Best School');
    ```
9.  **Count 89**
    *   Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
    *   The database name will be passed as an argument of the mysql command.
    *   File: `8-count_89.sql`
    ```
    -- Displays the number of records with id = 89 in the table first_table.
    SELECT COUNT(*) FROM first_table WHERE id = 89;
    ```

### Example SQL Script 📜
```sh
-- This script retrieves the first 3 students from Batch ID 3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Repo 🗂️

*   **GitHub Repository:** holbertonschool-higher\_level\_programming
*   **Directory:** SQL\_introduction

## Authors
[Saynez667](https://github.com/Saynez667)