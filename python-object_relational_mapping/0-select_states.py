#!usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
	# connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

	# Create a cursor
    cur = db.cursor()

    # SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    #  Get the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    db.close()
