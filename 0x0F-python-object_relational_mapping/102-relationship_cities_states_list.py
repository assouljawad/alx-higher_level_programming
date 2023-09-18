#!/usr/bin/python3
'''
script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
'''
from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # display tll states with cities
    data = session.query(State).order_by(State.id).all()
    i = 0
    for state in data:
        for city in state.cities:
            i += 1
            print("{}: {} -> {}".format(i, city.name, state.name))

    # close session
    session.close()
