class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0,0)):
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
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(p, int) and p >= 0 for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        for _ in range(self.__position[1]):
            print()
        for _  in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)