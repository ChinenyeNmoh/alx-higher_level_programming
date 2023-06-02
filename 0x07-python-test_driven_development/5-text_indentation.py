#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line_flag = True
    for i in text:
        if new_line_flag:
            if i == ' ':
                continue
            else:
                new_line_flag = False

        if not new_line_flag:
            if i in ['?', '.', ':']:
                print(i)
                print()
                new_line_flag = True
            else:
                print(i, end="")
