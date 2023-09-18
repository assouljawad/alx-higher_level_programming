#!/usr/bin/python3
''' file that contains the class definition of a
cities and an instance Base = declarative_base() '''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
    Cities class that inherits from Base
    Att:
        id : id of city
        name: name of the state
        state_id: id of state
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
