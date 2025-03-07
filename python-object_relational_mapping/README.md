## Project Title: Python Object-Relational Mapping 🚀

### Description 📝

This project focuses on utilizing Python to interact with MySQL databases through Object-Relational Mapping (ORM). It covers connecting to databases, performing CRUD operations, and mapping Python classes to database tables.

### Learning Objectives 🎯

By completing this project, you will be able to:

*   Connect to a MySQL database from a Python script 🐍
*   SELECT, INSERT, and UPDATE rows in a MySQL table 📊
*   Understand the concept of ORM 🧠
*   Map a Python Class to a MySQL table 🗺️

### Requirements ✅

*   **General**
    *   Allowed editors: `vi`, `vim`, `emacs`
    *   Ubuntu 20.04 LTS
    *   Python 3.8.5
    *   `MySQLdb` version 2.0.x
    *   `SQLAlchemy` version 1.4.x
    *   All files should end with a new line 📜
    *   First line: `#!/usr/bin/python3`
    *   A `README.md` file is mandatory 📌
    *   Code should follow `pycodestyle` (version 2.7.*)
    *   All files must be executable ⚙️
    *   Modules, classes, and functions must have documentation 📚
    *   No use of `execute` with SQLAlchemy

### Installation 🛠️

1.  **Install MySQL 8.0 on Ubuntu 20.04 LTS**

    ```
    sudo apt update
    sudo apt install mysql-server
    mysql --version
    ```
2.  **Connect to your MySQL server:**

    ```
    sudo mysql
    ```
3.  **Install MySQLdb module version 2.0.x**

    ```
    sudo apt-get install python3-dev
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install zlib1g-dev
    sudo pip3 install mysqlclient
    ```
4.  **Install SQLAlchemy module version 1.4.x**

    ```
    sudo pip3 install SQLAlchemy
    ```

### Usage 💻

Provide examples for each task, including sample code snippets and expected outputs.

### Tasks 📝

*   [x] **0. Get all states**: Lists all states from the database `hbtn_0e_0_usa`.
*   [x] **1. Filter states**: Lists all states starting with `N`.
*   [x] **2. Filter states by user input**: Displays values in the `states` table where the name matches the argument.
*   [x] **3. SQL Injection...**: Safe from MySQL injections!
*   [x] **4. Cities by states**: Lists all cities from the database `hbtn_0e_4_usa`.
*   [x] **5. All cities by state**: Lists all cities of that state.
*   [x] **6. First state model**: Contains the class definition of a `State`
*   [ ] **7. All states via SQLAlchemy**: Lists all State objects from the database `hbtn_0e_6_usa`.
*   [ ] **8. First state**: Prints the first `State` object from the database `hbtn_0e_6_usa`.
*   [ ] **9. Contains letter a**: Lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.
*   [ ] **10. Get a state**: Prints the `State` object with the name passed as argument from the database `hbtn_0e_6_usa`.
*   [ ] **11. Add a new state**: Adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
*   [ ] **12. Update a state**: Changes the name of a `State` object from the database `hbtn_0e_6_usa`.
*   [ ] **13. Delete states**: Deletes all `State` objects with a name containing the letter `e` from the database `hbtn_0e_6_usa`.
*   [ ] **14. Change comes from within**: Changes the name of a `City` object from the database `hbtn_0e_6_usa`.

### Author 👨‍💻

* [Saynez667](https://github.com/Saynez667)


