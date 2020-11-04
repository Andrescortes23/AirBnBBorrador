#!/usr/bin/python3
"""
Module to serializes instance to Json file and deserializes
Json file to a instance
"""
import json
import os.path


class FileStorage:
    """
    Class to Serializes and deserializes
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        Set __objects with obj as value and obj class name + .id as key
        """

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to Json file
        """

        newdict = {}
        for key, value in self.__objects.items():
            newdict[key] = value.to_dict()

        with open(self.__file_path, "w") as thefile:
            json.dump(newdict, thefile)

    def reload(self):
        """
        Deserializes Json file to __objects
        """

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if os.path.isfile(self.__file_path):
            from models.base_model import BaseModel

            with open(self.__file_path, "r") as thefile:
                objectfromjson = json.load(thefile)

            for key, value in objectfromjson.items():
                cls = value["__class__"]
                obj = eval(cls + "(**value)")
                self.__objects[key] = obj
        else:
            pass
