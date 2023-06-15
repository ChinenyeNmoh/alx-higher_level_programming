#!/usr/bin/python3
""" unit test class base """

import os
import unittest
from models.base import Base

class Testbase(unittest.TestCase):
    """Testing base"""
    def test_init(self):
        """testing initialization process"""
        #no argument
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

        #testing with a object defined id
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

        #Test with tuple
        self.assertEqual(Base((2, 3)).id, (2, 3))

        #test with list
        self.assertEqual(Base([2, 3]).id, [2, 3])

        #test with bool
        self.assertEqual(Base(True).id, True)

        #testing with None
        b4 = Base(None)
        self.assertEqual(b4.id, 3)
   
        #testing with range
        self.assertEqual(Base(range(5)).id, range(0, 5))

        #testing with float
        b5 = Base(3.3)
        self.assertEqual(b5.id, 3.3)

        #testing with str
        b6 = Base("4")
        self.assertEqual(b6.id, "4")

        #testing with private attribute
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)

        #testing with two arguments
        with self.assertRaises(TypeError):
            Base(2, 'b')

if __name__ == '__main__':
  unittest.main()
