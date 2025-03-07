#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the `states` table
of `hbtn_0e_0_usa` where `name` matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Récupération des arguments
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion à la base de données
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
    except MySQLdb.Error as e:
        print(f"Erreur de connexion: {e}")
        sys.exit(1)

    # Création d'un curseur
    cur = db.cursor()

    # Requête SQL avec format pour intégrer le nom d'état
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name_searched)

    # Exécution de la requête
    try:
        cur.execute(query)
    except MySQLdb.Error as e:
        print(f"Erreur d'exécution de la requête: {e}")
        cur.close()
        db.close()
        sys.exit(1)

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture des ressources
    cur.close()
    db.close()
