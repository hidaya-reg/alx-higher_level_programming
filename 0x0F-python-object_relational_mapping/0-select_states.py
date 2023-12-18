#!/usr/bin/python3
"""  Lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pd, db=db)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
