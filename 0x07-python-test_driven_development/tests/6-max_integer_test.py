#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_max_integer(self):
        """test list of ordered integers"""
        self.assertEqual(max_integer([5, 6, 9]), 9)

        """test list of unordered integers"""
        self.assertEqual(max_integer([5, 9, 5]), 9)

        """test single integer"""
        self.assertEqual(max_integer([100]), 100)

        """test list of floats"""
        self.assertEqual(max_integer([5.2, 6.7, 9.3]), 9.3)

        """test list of negative int"""
        self.assertEqual(max_integer([-5, -6, -9]), -5)

        """test list of negative float"""
        self.assertEqual(max_integer([-5.2, -6.7, -9.3]), -5.2)

        """test single string"""
        self.assertEqual(max_integer("123453276921"), "9")

        """test single string"""
        self.assertEqual(max_integer('abc'), 'c')

        """test for empty list"""
        self.assertIsNone(max_integer([]), None)

        """test for empty list"""
        self.assertIsNone(max_integer([None]), None)

        """test for list of  lists"""
        self.assertEqual(max_integer([[5, 6, 7], [5, 6, 7]]), [5, 6, 7])

        """test for exceptions"""
        with self.assertRaises(TypeError):
            max_integer(None)
        """test for exceptions"""
        with self.assertRaises(TypeError):
            max_integer([7, 1, 10, 16, None])


if __name__ == "__main__":
    unittest.main()
