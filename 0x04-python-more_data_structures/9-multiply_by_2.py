#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for i in a_dictionary.keys():
        res[i] = a_dictionary[i] * 2
    return res
