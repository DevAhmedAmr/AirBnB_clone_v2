#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""

        # print('save')
        temp = {}
        temp.update(self.__objects)

        for key, val in temp.items():
            # print(type(FileStorage.__objects[key].created_at))
            # print(type(val.created_at))
            if not isinstance(val, dict):
                # print('///////',type(val.created_at))
                temp[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)

                # print(self.all(), '1111')
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
            """
                print(
                    "storgeeeeeeee",
                    type(
                        self.__objects[
                            "State.a64667fa-782b-4f47-8853-f47be4c961ec"
                        ].created_at,
                    ),
                )
                """

        except FileNotFoundError:
            pass
            # print("FileStorage: FileNotFoundError")
