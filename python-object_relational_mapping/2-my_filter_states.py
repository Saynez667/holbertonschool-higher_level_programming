#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the `states` table
of `hbtn_0e_0_usa` where `name` matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Create the SQL query using format to include user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name_searched)

    # Execute the query
    cur.execute(query)

    # Fetch all results and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
