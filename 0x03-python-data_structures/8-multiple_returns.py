#!/usr/bin/python3
def multiple_returns(sentence):
    tup = tuple(sentence)
    length = len(tup)
    first = tup[0]
    if length == 0:
        first = None
    else:
        return (length, first)
