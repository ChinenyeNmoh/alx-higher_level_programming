#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        res = list(map(lambda i: i**2, i))
        newmatrix.append(res)
    return newmatrix
