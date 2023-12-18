#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, password, database = sys.argv[1:4]

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=database)

    cursor = db.cursor()

    query = '''
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    '''
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
