#!/usr/bin/python3
"""Defines unittests for models/square.py"""

from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testrectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""
    def test2_init(self):
        """ testing class Square logic"""

        """testing with no id argument"""
        self.assertEqual(Square(10, 2).id, 1)
        self.assertEqual(Square(4, 2, 3).id, 2)
        self.assertEqual(Square(2, 3, 4).id, 3)

        """testing with specified id"""
        self.assertEqual(Square(2, 4, 5, 11).id, 11)

        """testing id as str"""
        self.assertEqual(Square(1, 3, 4, '12').id, '12')

        """testing id with float"""
        self.assertEqual(Square(2, 2, 4, 4.5).id, 4.5)

        """testing size"""
        self.assertEqual(Square(2, 3, 4, 5).size, 2)

        """testing x"""
        self.assertEqual(Square(2, 3).x, 3)

        """testing y"""
        self.assertEqual(Square(2, 3).y, 0)

        """Instantiation with no args"""
        with self.assertRaises(TypeError):
            Square()

        """testing with private size"""
        with self.assertRaises(AttributeError):
            print(Square(5, 0, 0, 1).__size)

        """private x"""
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 1).__x)

        """private y"""
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 1).__y)

        """check subclass"""
        s = Square(2, 3, 4, 5)
        self.assertTrue(issubclass(type(s), Rectangle))

        """check instance"""
        self.assertIsInstance(s, Base)

        """tests if the class is actually square"""
        self.assertEqual(type(Square(3)), Square)

        """unittest for task3"""
    def test3init(self):
        """testing logic"""

        """testing setters"""
        s = Square(7, 9, 1, 2)
        s.size = 10
        self.assertEqual(s.size, 10)
        s.x = 3
        self.assertEqual(s.x, 3)
        s.y = 4
        self.assertEqual(s.y, 4)
        s.id = 5
        self.assertEqual(s.id, 5)

        """size is with non interger types"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)
            Square("8", 2)
            Square(complex(5 + 3j), 2)
            Square({"a": 5, "b": 2}, 2)
            Square((2, 3, 5, 7), 3)
            Square([2, 3, 5, 7], 3)
            Square({1, 3, 5, 7, 9}, 2)
            Square(True, 2)

        """x is with non interger types"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)
            Square(2, "8")
            Square(2, complex(5 + 3j))
            Square(3, {"a": 5, "b": 2})
            Square(1, (2, 3, 5, 7))
            Square(2, [2, 3, 5, 7])
            Square(4, {1, 3, 5, 7, 9})
            Square(4, True)

        """y is with non interger types"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 3, None)
            Square(4, 5, "8")
            Square(3, 3, complex(5 + 3j))
            Square(5, 6, {"a": 5, "b": 2})
            Square(3, 3, (2, 3, 5, 7))
            Square(5, 8, [2, 3, 5, 7])
            Square(7, 9, {1, 3, 5, 7, 9})
            Square(7, 9, True)

        """testing size with 0 and negetive numbers"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)
            Square(-1, 2)

        """testing x with  negative num"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(22, -3, 4)

        """testing y with  negative num"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -3)

        """unittest for task4"""
    def test_area(self):
        """testing area calculation"""
        self.assertEqual(Square(3, 2).area(), 9)
        self.assertEqual(Square(3, 2, 6, 7).area(), 9)

    """unittest for task 5 and 7"""
    def test_display(self):
        """tests the display method"""
        with StringIO() as display, redirect_stdout(display):
            Square(2).display()
            s = display.getvalue()
        self.assertEqual(s, "##\n##\n")
        with StringIO() as display, redirect_stdout(display):
            Square(2, 2, 2).display()
            s = display.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    """unittest for task6"""
    def test_str(self):
        """tests the str method"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(4, 2, id=12)
        self.assertEqual(s2.__str__(), "[Square] (12) 2/0 - 4")

    def test_update(self):
        """tests the update method"""
        s1 = Square(3, 1, 2, 12)
        self.assertEqual(str(s1), "[Square] (12) 1/2 - 3")
        s1.update(4)
        self.assertEqual(str(s1), "[Square] (4) 1/2 - 3")
        s1.update(id=10, size=3, x=2, y=4)
        self.assertEqual(str(s1), "[Square] (10) 2/4 - 3")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size="3")

    def test_to_dictionary(self):
        """tests the dictionary method"""
        s1 = Square(10, 2, 1, 7)
        s1_dictionary = s1.to_dictionary()
        string = "{'id': 7, 'size': 10, 'x': 2, 'y': 1}"
        self.assertEqual(str(s1_dictionary), string)
