# SQL_more_queries 🚀

This repository contains SQL scripts for various database querying and manipulation tasks. It's part of the Holberton School's higher-level programming curriculum. 

## Project Overview 📝

This project focuses on enhancing your SQL skills by tackling a series of challenges that involve creating databases, tables, and users, as well as writing complex queries.

## Tasks 🎯

Here's a breakdown of the tasks included in this project:

### 0. My privileges! 🔑
- **File:** `0-privileges.sql`
- **Description:** Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server (localhost).

### 1. Root user 👤
- **File:** `1-create_user.sql`
- **Description:** Creates the MySQL server user `user_0d_1` with all privileges and sets the password to `user_0d_1_pwd`.

### 2. Read user 📖
- **File:** `2-create_read_user.sql`
- **Description:** Creates the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privileges on `hbtn_0d_2`. Password is set to `user_0d_2_pwd`.

### 3. Always a name 🏷️
- **File:** `3-force_name.sql`
- **Description:** Creates the table `force_name` with columns `id` (INT) and `name` (VARCHAR(256), NOT NULL).

### 4. ID can't be null 🚫
- **File:** `4-never_empty.sql`
- **Description:** Creates the table `id_not_null` with columns `id` (INT, DEFAULT 1) and `name` (VARCHAR(256)).

### 5. Unique ID 🆔
- **File:** `5-unique_id.sql`
- **Description:** Creates the table `unique_id` with columns `id` (INT, DEFAULT 1, UNIQUE) and `name` (VARCHAR(256)).

### 6. States table 🗺️
- **File:** `6-states.sql`
- **Description:** Creates the database `hbtn_0d_usa` and the table `states` with columns `id` (INT, UNIQUE, AUTO_GENERATED, PRIMARY KEY) and `name` (VARCHAR(256), NOT NULL).

### 7. Cities table 🏙️
- **File:** `7-cities.sql`
- **Description:** Creates the table `cities` in `hbtn_0d_usa` with columns `id` (INT, UNIQUE, AUTO_GENERATED, PRIMARY KEY), `state_id` (INT, NOT NULL, FOREIGN KEY referencing `states.id`), and `name` (VARCHAR(256), NOT NULL).

### 8. Cities of California 🌴
- **File:** `8-cities_of_california_subquery.sql`
- **Description:** Lists all cities of California from the database `hbtn_0d_usa` using a subquery.

### 9. Cities by States 📍
- **File:** `9-cities_by_state_join.sql`
- **Description:** Lists all cities with their corresponding state names from the database `hbtn_0d_usa` using a JOIN.

### 10. Genre ID by show 🎬
- **File:** `10-genre_id_by_show.sql`
- **Description:** Lists all shows with at least one genre linked from the database `hbtn_0d_tvshows`.

### 11. Genre ID for all shows 📺
- **File:** `11-genre_id_all_shows.sql`
- **Description:** Lists all shows with their genre IDs from the database `hbtn_0d_tvshows`. Displays NULL if a show doesn't have a genre.

### 12. No genre 🚫
- **File:** `12-no_genre.sql`
- **Description:** Lists all shows without a genre linked from the database `hbtn_0d_tvshows`.

### 13. Number of shows by genre #️⃣
- **File:** `13-count_shows_by_genre.sql`
- **Description:** Lists all genres and the number of shows linked to each genre from the database `hbtn_0d_tvshows`.

### 14. My genres 🎭
- **File:** `14-my_genres.sql`
- **Description:** Lists all genres of the show Dexter from the database `hbtn_0d_tvshows`.

### 15. Only Comedy 🤣
- **File:** `15-only_comedy.sql`
- **Description:** Lists all shows that have the genre Comedy from the database `hbtn_0d_tvshows`.

### 16. Say my name 🗣️
- **File:** `16-no_link.sql`
- **Description:** Lists all records of the table `second_table` of the database `hbtn_0c_0`, excluding rows where the name column is empty, and displaying the score and name in descending order of score.

## Usage 🛠️

Each SQL script can be executed using the `mysql` command-line tool:
```sh
mysql -hlocalhost -uroot -p <database_name> < script_file.sql
```
Replace `<database_name>` with the appropriate database name and `<script_file.sql>` with the name of the SQL script you want to execute.

## Author ✍️

[Saynez667](https://github.com/Saynez667)
 - Holberton School Student