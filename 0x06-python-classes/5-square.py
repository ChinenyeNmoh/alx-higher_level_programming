#!/usr/bin/python3
""" this module represents a class square """


class Square:
    """Represents a square class """
    def __init__(self, size=0):
        """Initialize data with constructor"""

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
    def size(self, new_size):
        if type(new_size) != int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """ Returns the area of a square """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints # on stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
