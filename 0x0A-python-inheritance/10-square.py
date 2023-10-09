#!/usr/bin/python3
"""Create square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Create Square inherits from Rectangle class"""

    def __init__(self, size):
        """Instantite an square
        Args:
            size (int): size of square

        Returns:
            Square: New instance of square
        """
        
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Claculate area of a square"""
        return self.__size ** 2
