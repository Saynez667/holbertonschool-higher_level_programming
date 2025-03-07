#!/usr/bin/python3
"""
Script that safely fetches states matching a given name from `hbtn_0e_0_usa`,
preventing SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Main execution: Connects to MySQL, queries the
    database safely, and prints results. """

    # Get arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",  # MySQL server host
        port=3306,  # Default MySQL port
        user=mysql_username,  # MySQL username
        passwd=mysql_password,  # MySQL password
        db=database_name  # Database name
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name_searched,))

    # Fetch all results and print each row
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
