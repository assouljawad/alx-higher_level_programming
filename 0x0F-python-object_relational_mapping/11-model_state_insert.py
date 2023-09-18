#!/usr/bin/python3
'''
cript that adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # creat new state
    state = State(name="Louisiana")
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # add state
    session.add(state)
    session.commit()

    # print the new state id
    print("{}".format(state.id))

    # Close the session
    session.close()
