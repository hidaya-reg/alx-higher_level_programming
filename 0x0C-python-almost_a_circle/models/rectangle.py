#!/usr/bin/python3
"""Class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        self.validate_attr("width", value, False)
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter of height"""
        self.validate_attr("height", value, False)
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter of x"""
        self.validate_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setter of y"""
        self.validate_attr("y", value)
        self.__y = value

    def validate_attr(self, attr, value, is_xy=True):
        """Valdate attributes"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if is_xy and value < 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif not is_xy and value <= 0:
            raise ValueError("{} must be > 0".format(attr))

