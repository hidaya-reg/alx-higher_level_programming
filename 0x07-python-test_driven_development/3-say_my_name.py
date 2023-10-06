#!/usr/bin/python3
"""function that prints My name"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional)

    Raises:
        TypeError: If first_name or last_name is not a string
    """

    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = "{} {}".format(first_name, last_name)
    else:
        full_name = first_name

    print("My name is {}".format(full_name))
