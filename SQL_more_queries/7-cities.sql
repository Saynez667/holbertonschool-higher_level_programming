-- This script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- That create the tables cities in the database hbtn_0d_usa with the following requirements:
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
