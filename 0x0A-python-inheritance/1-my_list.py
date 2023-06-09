#!/usr/bin/python3
"""Creating function print_sorted"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """print_sorted method."""
        list2 = []
        for i in sorted(self):
            list2.append(i)
        print(list2)
