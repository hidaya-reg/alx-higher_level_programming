#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """add two integers

    Args:
        a (int or float): the first number to be added
        b (int or float, optional): second number

    Returns:
        int: sum of a and b, cast to integer

    Raises:
        TypeError: if `a` and `b` not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
