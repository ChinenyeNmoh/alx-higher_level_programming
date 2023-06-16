#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""

from io import StringIO
import sys
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    def test2_init(self):
        """ testing class Rectangle logic"""

        #testing with no id argument
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(4, 2, 3).id, 2)
        self.assertEqual(Rectangle(2, 3, 4, 5).id, 3)

        #testing with specified id
        self.assertEqual(Rectangle(2, 3, 4, 5, 11).id, 11)

        #testing id as str
        self.assertEqual(Rectangle(2, 1, 3, 4, '12').id, '12')

        #testing id with float
        self.assertEqual(Rectangle(2, 1, 2, 4, 4.5).id, 4.5)

        #testing width
        self.assertEqual(Rectangle(2, 3, 4, 5).width, 2)

        #testing height
        self.assertEqual(Rectangle(2, 3, 4, 5).height, 3)

        #testing x
        self.assertEqual(Rectangle(2, 3).x, 0)

        #testing y
        self.assertEqual(Rectangle(2, 3).y, 0)

        #Instantiation with no args.
        with self.assertRaises(TypeError):
            Rectangle()

        #Instantiation missing one arg.
        with self.assertRaises(TypeError):
            Rectangle(1)

        #testing with private width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

        #testing with private height
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

        #private x
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1).__x)

        #private y
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1).__y)

        #check subclass
        r = Rectangle(2, 3, 4, 5)
        self.assertTrue(issubclass(type(r), Base))

        #check instance
        self.assertIsInstance(r,Base)

        """unittest for task3"""
    def test3init(self):
        """testing logic"""
    
        #testing setters
        r = Rectangle(3, 7, 9, 1, 2)
        r.width = 10
        self.assertEqual(r.width, 10)
        r.height = 2
        self.assertEqual(r.height, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        r.y = 4
        self.assertEqual(r.y, 4)
        r.id = 5
        self.assertEqual(r.id, 5)

        #width is with non interger types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
            Rectangle("8", 2)
            Rectangle(complex(5 + 3j), 2)
            Rectangle({"a": 5, "b": 2}, 2)
            Rectangle((2, 3, 5, 7), 3)
            Rectangle([2, 3, 5, 7], 3)
            Rectangle({1, 3, 5, 7, 9}, 2)
            Rectangle(True, 2)

        #height is with non interger types
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
            Rectangle(2, "8")
            Rectangle(2, complex(5 + 3j))
            Rectangle(2, {"a": 5, "b": 2})
            Rectangle(3, (2, 3, 5, 7))
            Rectangle(3, [2, 3, 5, 7])
            Rectangle(2, {1, 3, 5, 7, 9})
            Rectangle(2, False)

        #x is with non interger types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)
            Rectangle(2, 4, "8")
            Rectangle(2, 3, complex(5 + 3j))
            Rectangle(3, 5, {"a": 5, "b": 2})
            Rectangle(1, 3, (2, 3, 5, 7))
            Rectangle(2, 5, [2, 3, 5, 7])
            Rectangle(4, 7, {1, 3, 5, 7, 9})
            Rectangle(4, 7, True)

        #y is with non interger types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 3, None)
            Rectangle(2, 4, 5, "8")
            Rectangle(2, 3, 3, complex(5 + 3j))
            Rectangle(3, 5, 6, {"a": 5, "b": 2})
            Rectangle(1, 3, 3, (2, 3, 5, 7))
            Rectangle(2, 5, 8, [2, 3, 5, 7])
            Rectangle(4, 7, 9, {1, 3, 5, 7, 9})
            Rectangle(4, 7, 9, True)        

        #testing width with 0 and negetive numbers
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
            Rectangle(-1, 2)

        #testing height with 0 and negative num
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
            Rectangle(2, -3)

        #testing x with  negative num
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(22, 3, -3, 4)

        #testing y with  negative num
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(22, 3, 4, -3)

        """unittest for task4"""
    def test_area(self):
        """testing area calculation"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(3, 2, 6, 7, 1).area(), 6)
 
    """unittest for task 5 and 7"""
    def test_display__method(self):
        """display, without 'x' and 'y' """
        r1 = Rectangle(2, 3)
        capture = StringIO()
        with redirect_stdout(capture):
            r1.display()
        self.assertEqual(capture.getvalue(), "##\n##\n##\n")

        #display, with 'x' and 'y'
        r1 = Rectangle(2, 3, 1, 2)
        capture = StringIO()
        with redirect_stdout(capture):
            r1.display()
        self.assertEqual(capture.getvalue(), "\n\n ##\n ##\n ##\n")

    """unittest for task6"""
    def test_str(self):
        """tests the str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(4, 6, 2, id=12)
        self.assertEqual(r2.__str__(), "[Rectangle] (12) 2/0 - 4/6")

    def test_update(self):
        """tests the update method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(8)
        self.assertEqual(str(r1), "[Rectangle] (8) 10/10 - 10/10")
        r1.update(89, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 4/10")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, "3", 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, 3, -4, 5)

    def test_updateargs(self):
        """tests the update with args and kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/10")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height="3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-3)

    def test_to_dictionary(self):
        """tests the dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        s = "{'id': 89, 'width': 10, 'height': 2, 'x': 1, 'y': 9}"
        self.assertEqual(str(r1_dictionary), s)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (89) 1/9 - 10/2")
