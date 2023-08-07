#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
import datetime


class BaseModel:
    """Represents the BaseModel of HBnB project."""
    def __init__(self):
        """
        Initialize a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the BaseModel object.
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary representation.
        Dictionary will contain all keys and values of the instance attribute.
        __class__ key will be added with the class name of the object.
        The created_at and updated_at will be converted to
        string objects in ISO format.
        """
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.created_at.isoformat()
        return dicts
