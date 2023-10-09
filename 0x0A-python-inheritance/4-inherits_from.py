#!/usr/bin/python3
"""Verify if object is instance of inherited class"""


def inherits_from(obj, a_class):
    """Verify if object is instance of inherited class

    Args:
        obj (object): object to verify
        a_class (class): class to lookup

    Return:
        bool: True if obj is instance of a class that
            inherited from a_class
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
