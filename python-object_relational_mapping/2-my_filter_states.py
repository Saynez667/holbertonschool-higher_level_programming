#!/usr/bin/python3
"""
Script that lists all states with a name matching the user input from
the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states_by_user_input():
    """Function that filters states by user input"""
    if len(sys.argv) != 5:
        return

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor
    cur = db.cursor()

    state_name = sys.argv[4]

    # Execute the query using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Get and print the results
    for row in cur.fetchall():
        print(row)

    # Close all cursors and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_user_input()
