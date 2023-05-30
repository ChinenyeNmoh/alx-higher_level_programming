#!/usr/bin/python3
""" this module represents a class square """


class Square:
    """Represents a square class """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                        )
            self.__position = value

    def area(self):
        """ Returns the area of a square """
        return (self.__size * self.__size)

    def my_print(self):
        size = self.__size
        lines = self.__position[1]
        spaces = self.__position[0]
        if size == 0:
            print()
        for newlines in range(lines):
            print()
        for row in range(size):
            print((' ' * spaces) + ('#' * size))
