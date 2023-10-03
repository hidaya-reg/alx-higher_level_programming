#!/usr/bin/python3
"""defines a class `LockedClass` that restricts
the creation of instance attributes.
"""


class LockedClass:
    """A class that restricts the creation of instance attributes."""
    __slots__ = ('first_name',)
