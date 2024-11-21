#!/usr/bin/python3
"""Base Model for the AirBnB Clone"""


from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialization of the class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string presentation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing key/values of __dict__"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__

        if not isinstance(my_dict["created_at"], str):
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if not isinstance(my_dict["updated_at"], str):

            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
