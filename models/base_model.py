#!/usr/bin/python3
"""This model represents the base model of the hbnb"""
from models import storage
import uuid
from datetime import datetime as dt


class BaseModel:
    """The base class defining common attributes for all other classes"""
    name = None
    my_number = None

    def __init__(self, *args, **kwargs):
        """initalizes instances when class is created"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__' and value:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Representation of the Basemodel"""
        me = '[' + str(type(self).__name__) + '] ' + '(' + self.id + ') '
        return me + str(self.__dict__)

    def save(self):
        """updates the time the object is changed"""
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """returns all instance attributes including unset"""
        my_dict = dict()
        my_dict['name'] = self.name
        my_dict['my_number'] = self.my_number
        my_dict['id'] = self.id
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = dt.isoformat(self.created_at)
        my_dict['updated_at'] = dt.isoformat(self.updated_at)
        return my_dict
