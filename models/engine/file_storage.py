#!/usr/bin/python3
"""serializes and deserializes json to and from file"""
import json
import os


class FileStorage:
    """This class performs serialization and deserialization of dicts"""
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """returns the dictionary  representation"""
        return self.__objects

    def new(self, obj):
        """add the new object to the dictionary __objects"""
        key = str(type(obj).__name__) + '.' + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """save dictionary to json file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialize dictionary from string in file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                try:
                    self.__objects = json.load(f)
                except Exception:
                    pass
