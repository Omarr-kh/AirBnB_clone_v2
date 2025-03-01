#!/usr/bin/python3
''' City Module for HBNB project '''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    ''' The City Class '''
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id', ondelete='CASCADE'),
                          nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ''
        state_id = ''
