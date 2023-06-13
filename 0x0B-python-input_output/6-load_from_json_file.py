#!/usr/bin/python3
""" function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """ return data from json file """
    with open(filename, mode="r", encoding="utf-8") as rf:
        return json.load(rf)
