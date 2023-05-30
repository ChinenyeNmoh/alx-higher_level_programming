#!/usr/bin/python3
""" this module represents a class square """


class Square:
    """Represents a square class """
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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

    def area(self):
        """ Returns the area of a square """
        return self.__size * self.__size
