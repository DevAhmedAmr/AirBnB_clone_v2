#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):  # "Create State name = California"
        """Instatntiates a new model"""
        if not kwargs or "id" not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            for key, value in kwargs.items():
                if key != "created_at" and key != "updated_at":
                    setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)

            del kwargs["__class__"]

            """
            self.__dict__.update(kwargs)
            """

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        # print(type(self.created_at), '################')
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        # print(type(self.created_at), '************')
        # print(type(self))
        # if isinstance(self.created_at, str):
        # self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        # print("finaal", self.id, self.created_at, type(self.created_at))
        dictionary["created_at"] = self.created_at.isoformat()
        # if isinstance(self.updated_at, str):
        # self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
