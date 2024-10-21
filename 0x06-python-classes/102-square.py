#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """Initialize a new square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Calculate the area of the suare
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __lt__(self, other):
        """Check if this square is less than another square"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Check if this square is less than or equal to another square"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Check if this square is greater than another square"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Check if this square is greater than or equal to another square"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
