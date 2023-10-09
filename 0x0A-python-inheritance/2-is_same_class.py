#!/usr/bin/python3
"""Verify if the object is exactly an instance
of the specified class"""


def is_same_class(obj, a_class):
    """verify if object is instance of given class

    Args:
        obj (object): object to verify it's class
        a_class (class): THe class to verify if obj is
                        instanceof

    Returns:
        bool: True if obj is instance of a_class, False otherwise
    """
    return type(obj) is a_class
