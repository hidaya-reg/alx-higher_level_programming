#!/usr/bin/python3
"""Create BaseGeometry class"""


class BaseGeometry:
    """Create BaseGeometry class"""

    def area(self):
        """raises an Exception
        Raises:
            Exception: Not implemeted
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name (str): name
            value (int): value of name

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
