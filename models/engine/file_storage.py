#!usr/bin/python3
"""Defines the FileStorage class."""
from models.base_model import BaseModel
import json


class FileStorage:
    """Represents an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Desrialize the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for obj_data in objects.values():
                    name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(name)(**obj_data))
        except FileNotFoundError:
            pass
