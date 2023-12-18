#!/usr/bin/python3
"""Deletes State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State, City).filter(State.id == City.state_id) \
                    .order_by(City.id).all()

    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
