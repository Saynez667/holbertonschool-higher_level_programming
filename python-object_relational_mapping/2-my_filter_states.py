#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor
    cur = db.cursor()

    state_name = sys.argv[4]

    # SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY stade.id ASC".format(state_name))

    # Fetch and display the results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
