#!/usr/bin/python3
''' Place Module for HBNB project '''
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Table, String, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    ''' The Place class '''
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenity_ids = []

    @property
    def reviews():
        '''Retrieve all reviews associated with this place'''
        all_reviews = storage.all(Review)
        place_reviews = []

        for rev in all_reviews.values():
            if rev.place_id == self.id:
                place_reviews.append(rev)

        return place_reviews
