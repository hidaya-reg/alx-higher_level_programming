#!/usr/bin/python3
"""Create Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """function that assign attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return a dictionary representation of the Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
