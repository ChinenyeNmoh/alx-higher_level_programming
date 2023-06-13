#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

import json


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    json_data = json.dumps(obj.__dict__)
    return json_data
