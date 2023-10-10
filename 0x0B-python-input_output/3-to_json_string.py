#!/usr/bin/python3
"""function that returns the JSON representation
of an object"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj: object to be converted to JSON

    Returns:
        A JSON-formatted string representing the input object
    """
    return json.dumps(my_obj)
