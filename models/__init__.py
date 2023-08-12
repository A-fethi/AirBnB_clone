#!/usr/bin/python3
"""Reloads the storage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"User": User, "BaseModel": BaseModel,
           "Amenity": Amenity, "State": State,
           "Place": Place, "City": City,
           "Review": Review}

storage = FileStorage()
storage.reload()
