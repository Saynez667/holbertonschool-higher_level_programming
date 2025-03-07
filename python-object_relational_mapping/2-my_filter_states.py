#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from
the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states_by_user_input():
    """Function that filters states by user input"""
    if len(sys.argv) != 5:
        return

    #  Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor
    cur = db.cursor()

    state_name = sys.argv[4],

    # Execute the query
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    )

    # Get the results
    for row in cur.fetchall():
        print(row)

    # Close all cursors
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_user_input()
