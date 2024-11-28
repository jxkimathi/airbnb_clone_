#!/usr/bin/python3
"""The Place model in the AirBnB Project"""
from models.base_model import BaseModel

class Place(BaseModel):
    """The Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    desription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
