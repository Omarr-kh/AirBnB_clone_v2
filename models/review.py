#!/usr/bin/python3
''' Review module for the HBNB project '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' The Review class '''
    place_id = ""
    user_id = ""
    text = ""
