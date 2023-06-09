#!/usr/bin/python3
"""3-is_kind_of_class.py module"""


def is_kind_of_class(obj, a_class):
    """Function that checks of object is instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
