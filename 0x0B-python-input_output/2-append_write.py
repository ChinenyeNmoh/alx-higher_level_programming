#!/usr/bin/python3
""" append module """


def append_write(filename="", text=""):
    """ add a string at the end of the line """
    with open(filename, mode="a", encoding="utf-8") as af:
        return af.write(text)
