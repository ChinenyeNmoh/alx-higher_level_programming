#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    len = 0
    for i in str:
        if len != n:
            string += i
        len += 1
    return string
