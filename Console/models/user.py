#!/usr/bin/python3
"""The user model for the AirBnB app"""

from models.base_model import BaseModel

class User(BaseModel):
    """The User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
