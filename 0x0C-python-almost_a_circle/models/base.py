#!/usr/bin/python3
"""Create first class Base"""


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
