#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(p, int) and p >= 0 for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Set the positionof the square
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(p, int) and p >= 0 for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def __str__(self):
        """Return representation of square as string
        """
        
        if self.__size == 0:
            return ""
        
        s = ""
        s += "\n" * self.__position[1]

        for _ in range(self.__size):
            s += " " * self.__position[0] + "#" * self.__size + "\n"
        return s.strip()
