#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int, optional): size of the square
            position (tuple, optional): position of square
        """

        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """Get the position of the square

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the positionof the square

        Args:
            value (tuple): the position to set

        Raises:
            TypeError: If value is not a tupleof two positives
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the suare

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the #
        If size = 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
