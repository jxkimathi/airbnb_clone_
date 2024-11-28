#!/usr/bin/python3
"""Storage File for the data"""
import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class_name>.id"""
        id = obj.to_dict()["id"]
        classname = obj.to_dict()["__class__"]
        keyname = classname + "." + id
        FileStorage.__objects[keyname] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        # Convert the objects to dictionaries
        for key, value in data.items():
            data[key] = value.to_dict()
        # Serialize the dictionaries to JSON
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """Deserealizes the JSON file to __objects"""
        path = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as file:
                    for key, value in json.load(file).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
            except Exception:
                pass
