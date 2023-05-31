#!/usr/bin/python3
'''class definitions'''
import math


class MagicClass:
    '''defining class: MagicClass'''

    """initializing method"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    """Return the area of the MagicClass"""
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """Return The circumference of the MagicClass."""
    def circumference(self):
        return (self.__radius * 2 * math.pi)
