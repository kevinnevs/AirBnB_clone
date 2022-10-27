#!/usr/bin/python3
"""
Serializes instances to a JSON file & deserializes JSON file to instances
"""
import json



class FileStorage:
    """
    private class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets __objects the obj with key <obj class name>.id
        """
        name = obj.__class__.__name__
        FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        jsonData = {}
        for key, value in FileStorage.__objects.items():
            jsonData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            data = json.dump(jsonData, f)

    def reload(self):
        """
        deserliazes the JSON file to __objects
        does nothing if file(__file_path) doesn't exist
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    self.new(eval(obj['__class__'])(**obj))
        except:
            return