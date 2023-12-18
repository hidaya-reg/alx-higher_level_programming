#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, password, database = sys.argv[1:4]

    db = MySQLdb.connect(
            host=host, port=port,
            user=user, password=password,
            db=database)
    cursor = db.cursor()

    query = "SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY `id`"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
