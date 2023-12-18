#!/usr/bin/python3
""" script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=database)

    cursor = db.cursor()

    query = "SELECT * from states WHERE `name` = '{}' "\
            "ORDER BY `id`".format(state_name)
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
