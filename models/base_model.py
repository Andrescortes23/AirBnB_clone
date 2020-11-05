#!/usr/bin/python3
"""
Base class for models
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    Class BaseModel with all attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """Objects constructor to set:
        ================
        id: assign with an uuid when an instance is created

        created_at: assign with the current datetime when instance is created

        updated_at: assign with the current datetime when an instance
        is created and it will be updated every time you change your object


        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Method to return a string representation. should print:
        [<class name>] (<self.id>) <self.__dict__>
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method to update the attribute update_at with current date time
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Method to returns a dictionary containing all keys/values of
        __dict__ of the instance
        """

        dicto = dict(self.__dict__)
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.isoformat()
        dicto["updated_at"] = self.updated_at.isoformat()
        return dicto
