#!/usr/bin/python3
"""
Contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r') as f:
        new_list = []
        while True:
            line = f.read()
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
    with open(filename, 'w') as f:
        f.writelines(new_list)
