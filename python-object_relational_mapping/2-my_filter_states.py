#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (safe from SQL injections).
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

    # Get the state name
    state_name = sys.argv[4]

    # Excexuter a query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )

    cur.execute(query)

    # get the results
    for row in cur.fetchall():
        print(row)

    # Close all cursors
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_user_input()
