#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of rectangle

        Args:
            value (int): the new width

        Raises:
            TypeError: if value is not integr
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve height of rectangle

        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set thze height of the rzctangle

        Args:
            value (int): height of rectangle

        Raises:
            TypeError: if value not integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
