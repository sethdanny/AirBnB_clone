#!/usr/bin/python3
""" A Base class with common methods / attributies Module for our BaseModel """


import uuid
from datetime import datetime, time, date


class BaseModel():
    """ a class which defines attribuites id,
     created_at, updated_at and methods """

    def __init__(self, *args, **kwargs):
        """ constructor method for class attributes id,
         created_at, updated_at """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """ returns the string representation of the model """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the updated_at attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys and values """
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
        })
        return my_dict
