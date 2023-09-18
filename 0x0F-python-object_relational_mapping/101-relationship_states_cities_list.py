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
    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # close session
    session.close()
