#!/usr/bin/python3
"""Create first class Base"""
import json


class Base:
    """Basic class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
