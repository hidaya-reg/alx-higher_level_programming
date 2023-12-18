#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=u, password=p, db=d)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
