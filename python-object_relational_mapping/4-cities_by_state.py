#!/usr/bin/python3
"""
Script that lists all cities from the database `hbtn_0e_4_usa`,
including the corresponding state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    """ Get arguments from the command line """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """ Connect to MySQL database """
    db = MySQLdb.connect(
        host="localhost",  # MySQL server host
        port=3306,  # Default MySQL port
        user=mysql_username,  # MySQL username
        passwd=mysql_password,  # MySQL password
        db=database_name  # Database name
    )

    """ Create a cursor object to execute SQL queries """
    cur = db.cursor()

    """Execute a query to retrieve cities and their state names, ordered
    by cities.id"""
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    """ Fetch all results and print each row """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Close the cursor and database connection """
    cur.close()
    db.close()
