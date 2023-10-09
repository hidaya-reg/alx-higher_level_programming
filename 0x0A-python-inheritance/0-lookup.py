#!/usr/bin/python3
"""return the list of attributes and methodes of an obj"""


def lookup(obj):
    """
    returns list of atts and methods of obj

    Args:
        obj (object): objcet to look up

    Returns:
        list: list of available objects and methods
    """
    return dir(obj)
