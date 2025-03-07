#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def filter_states():
    """Function that lists states starting with 'N'"""
    if len(sys.argv) != 4:
        return

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

    # SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and display the results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    filter_states()