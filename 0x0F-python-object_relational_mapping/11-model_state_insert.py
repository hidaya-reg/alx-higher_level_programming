#!/usr/bin/python3
""" Lists all State objects with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print(new_state.id)

    session.close()
