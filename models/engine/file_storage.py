import json
import os.path


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
       return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        newdic =
        with open(self.__file_path, "w") as thefile:
            json.dump(self.__objects, thefile)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as thefile:
                self.__objects = json.load(thefile)
        else:
            pass
