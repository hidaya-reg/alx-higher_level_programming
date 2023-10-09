#!/usr/bin/python3
"""Create Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Create Rectangle inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantite an object
        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Returns:
            Rectangle: New instance of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
