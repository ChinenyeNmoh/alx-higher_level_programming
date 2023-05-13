#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for i in my_string:
        if i in 'cC':
            continue
        newstring += i
    return newstring
