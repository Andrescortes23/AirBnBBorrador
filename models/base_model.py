import uuid
from models import storage
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for a in kwargs:
                if a is "id":
                    self.id = kwargs[a]
                elif a is "created_at":
                    self.created_at = datetime.strptime\
                                      (kwargs[a], "%Y-%m-%dT%H:%M:%S.%f")
                elif a is "my_number":
                    self.my_number = kwargs[a]
                elif a is "updated_at":
                    self.updated_at = datetime.strptime\
                                      (kwargs[a], "%Y-%m-%dT%H:%M:%S.%f")
                elif a is "name":
                    self.name = kwargs[a]
        else:
            storage.new(self)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()



    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        dicto = self.__dict__
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.isoformat()
        dicto["updated_at"] = self.updated_at.isoformat()
        return dicto
