#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys


def connectDb(user, password, db):
    """
    Connect to MySQL database
    
    Args:
        user (str): MySQL username
        password (str): MySQL password
        db (str): Database name
        
    Returns:
        Connection: MySQL database connection
    """
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )


if __name__ == "__main__":
    # Get command line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    # Connect to database
    conn = connectDb(user, password, db)
    cursor = conn.cursor()

    # %s is a placeholder for the state name, preventing SQL injection
    query = """ SELECT * FROM states WHERE states.name = %s
        ORDER BY states.id ASC
    """
    cursor.execute(query, (arg,))

    # Fetch all the results of the query
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
