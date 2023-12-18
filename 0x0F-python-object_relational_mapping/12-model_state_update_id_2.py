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

    state_to_update = session.query(State).filter_by(id=2).first()

    state_to_update.name = "New Mexico"

    session.commit()

    session.close()
