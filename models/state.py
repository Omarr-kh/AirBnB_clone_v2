#!/usr/bin/python3
''' State Module for HBNB project '''
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    ''' The State class '''
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all", backref="state")

    @property
    def cities(self):
        '''Retrieve all cities associated with this state'''
        dict_objs = storage.all(City)
        state_cities = []

        for city in dict_objs.values():
            if city.state_id == self.id:
                state_cities.append(city)

        return state_cities
