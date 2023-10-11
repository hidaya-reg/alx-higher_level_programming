#!/usr/bin/python3
"""unction that writes an Object to a text file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to txt file, using JSON representation

    Args:
    my_obj (object): python object
    filename (str): file to write JSON representation of my_obj
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
