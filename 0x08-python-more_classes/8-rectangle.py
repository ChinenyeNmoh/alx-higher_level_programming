#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the new width value"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new height value"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return (self.__width * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        max = rect_1
        if rect_1.area() < rect_2.area():
            max = rect_2
        if rect_1.area() == rect_2.area():
            max = rect_1
        return max

    def perimeter(self):
        """returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints string representation of instances"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for j in range(self.__height))

    def __repr__(self):
        """prints the official representation of object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
