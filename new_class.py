#!/usr/bin/python3
"""creates class from the available list"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


def new_class(obj, dicts=None):
    """create a new object with or without dictionary"""
    if obj == 'BaseModel':
        if dicts is None:
            a = BaseModel()
        else:
            a = BaseModel(**dicts)
    elif obj == 'State':
        if dicts is None:
            a = State()
        else:
            a = State(**dicts)
    elif obj == 'Place':
        if dicts is None:
            a = Place()
        else:
            a = Place(**dicts)
    elif obj == 'City':
        if dicts is None:
            a = City()
        else:
            a = City(**dicts)
    elif obj == 'Amenity':
        if dicts is None:
            a = Amenity()
        else:
            a = Amenity(**dicts)
    elif obj == 'Review':
        if dicts is None:
            a = Review()
        else:
            a = Review(**dicts)
    elif obj == 'User':
        if dicts is None:
            a = User()
        else:
            a = User(**dicts)
    return a
