import json
import os.path
#from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
       return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        newdict = {}
        for key, value in self.__objects.items():
            newdict[key] = value.to_dict()

        with open(self.__file_path, "w") as thefile:
            json.dump(newdict, thefile)

    def reload(self):
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
