#!/usr/bin/python
# Lists all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
