#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute to an object if it's possible

    Args:
        obj (object): object to which attribute should be aded
        attribute (str): name of attribute to add
        value (any): value of the new attribute

    Raises:
        TypeError: If object cannot have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
