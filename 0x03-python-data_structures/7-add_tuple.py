#!/usr/bin/python3
def add_tuples(tuple_a, tuple_b):
    if len(tuple_a) < 2:
        tuple_a = (0, 0)
    if len(tuple_b) < 2:
        tuple_b = (0, 0)
    add1 = tuple_a[0] + tuple_b[0]
    add2 = tuple_a[1] + tuple_b[1]
    return add1, add2