#!/usr/bin/python3
"""function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """Convert obj to a JSON-serializable dictionary"""
    json_dict = {}
    class_dict = obj.__dict__

    for k, v in class_dict.items():
        if isinstance(v, (list, dict, str, int, bool)):
            json_dict[k] = v

    return json_dict
