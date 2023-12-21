#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
