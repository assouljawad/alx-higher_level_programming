#!/usr/bin/python3
'''
script that prints the first State object from the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get first state
    first = session.query(State).order_by(State.id).first()

    # Check if a State was found
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
