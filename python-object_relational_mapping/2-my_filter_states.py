#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database hbtn_0e_0_usa"""

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

    state_name= sys.argv[4]

    # SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY stade.id ASC".format(state_name))

    # Fetch and display the results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
