from modeltest.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_attr(name, value, is_xy=True):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if is_xy and value < 0:
            raise ValueError(f'{name} must be >= 0')
        elif not is_xy and value <= 0:
            raise ValueError(f'{name} must be > 0')

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.validate_attr('width', width, False)
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.validate_attr('height', height, False)
        self.__height = height
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.validate_attr('x', x)
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.validate_attr('y', y)
        self.__y = y

    def area(self):
        return self.__height * self.__width
    
    def display(self):

        display = (' ' * self.__x + '#' * self.__width + '\n') * self.__height
        print('\n' * self.__y, end='')
        print(display, end='')

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        attrs = ["id", "width", "height", "x", "y"]

        return {k: getattr(self, k) for k in attrs}
