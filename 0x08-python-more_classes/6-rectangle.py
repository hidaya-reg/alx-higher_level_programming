#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculate and return area of rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
            int:: perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Return formal representation of the rectangle

        Returns:
            str: formal string representing rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
