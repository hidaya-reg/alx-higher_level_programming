#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dict representation current student"""
        json_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, dict, str, list, bool)):
                json_dict[k] = v
        return json_dict
