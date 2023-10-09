#!/usr/bin/python3
"""Verify if object is instance of class"""


def is_kind_of_class(obj, a_class):
    """Verify if object is instance of class

    Args:
        obj (object): object to verify
        a_class (class): class to lookup

    Returns:
        bool: True if obj instance of a_class,
            False otherwise
    """
    return isinstance(obj, a_class)
