#!/usr/bin/python3
"""Defines a JSON-to-object function."""


import json


def from_json_string(my_str):
    """ convert json file to python dict """
    return json.loads(my_str)
