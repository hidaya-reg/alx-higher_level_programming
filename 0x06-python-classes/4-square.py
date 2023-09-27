#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int, optional): size of the square
        """

        self.size = size

    @property
    def size(self):
        """Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The size to set

        Raises:
            TypeError: If value is not integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the suare

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
