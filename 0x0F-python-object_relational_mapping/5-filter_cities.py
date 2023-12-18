#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, password, database = sys.argv[1:4]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=database)

    cursor = db.cursor()

    query = '''
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = %s
    ORDER BY cities.id
    '''
    cursor.execute(query, (state_name,))
    cities = cursor.fetchone()[0]

    if cities:
        print(cities)

    cursor.close()
    db.close()
