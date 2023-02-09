#!/usr/bin/python3
""" module for filestorage class """

import json


class FileStorage():
    """ filestorage class """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ defines our constructor """
        pass

    def all(self):
        """ gets all attributies """
        return FileStorage.__objects

    def new(self, obj):
        """ registers a new object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ saves all objects to a file """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """ deserialize from a json file """
        from models.base_model import BaseModel

        class_dict = {"BaseModel":BaseModel}
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
