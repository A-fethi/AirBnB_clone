#!usr/bin/python3
'''
    Defines the FileStorage class
'''
import models
import json


class FileStorage:
    '''
        Represents an abstracted storage engine.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            Return the dict __objects.
        '''
        return self.__objects

    def new(self, obj):
        '''
            Set in __objects obj with key <obj_class_name>.id
        '''
        key = f"{str(obj.__class__.__name__)}.{str(obj.id)}"
        dict_val = obj
        FileStorage.__objects[key] = dict_val

    def save(self):
        '''
            Serialize __objects to the JSON file.
        '''
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF8") as f:
            json.dump(data, f)

    def reload(self):
        '''
            Desrialize the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    name = value["__class__"]
                    name = models.classes[name]
                    FileStorage.__objects[key] = name(**value)
        except FileNotFoundError:
            pass
