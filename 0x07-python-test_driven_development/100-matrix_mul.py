#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    msg = [
            'm_a must be a list',
            'm_b must be a list',
            'm_a must be a list of lists',
            'm_b must be a list of lists',
            'm_a can\'t be empty',
            'm_b can\'t be empty',
            'm_a should contain only integers or floats',
            'm_b should contain only integers or floats',
            'each row of m_a must be of the same size',
            'each row of m_b must be of the same size',
            'm_a and m_b can\'t be multiplied',
            ]

    """checks if m_a is a list"""
    if not isinstance(m_a, list):
        raise TypeError(msg[0])

    """checks if m_b is a list"""
    if not isinstance(m_b, list):
        raise TypeError(msg[1])

    """ checks if m_a is list of lists"""
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError(msg[2])

    """ checks if m_b is list of lists"""
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError(msg[3])

    """checks if m_a is empty or any of its lists is empty"""
    if m_a == [] or m_a == [[]]:
        raise ValueError(msg[4])

    """checks if m_b is empty or any of its lists is empty"""
    if m_b == [] or m_b == [[]]:
        raise ValueError(msg[5])

    """checks if all the elements in the m_a are int or float"""
    if not all(
            isinstance(element, (int, float)) for row in m_a for element in row
            ):
        raise TypeError(msg[6])

    """checks if all the elements in the m_b are int or float"""
    if not all(
            isinstance(element, (int, float))for row in m_b for element in row
            ):
        raise TypeError(msg[7])

    """checks if all the rows in m_a has equal length"""
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError(msg[8])

    """checks if all the rows in m_b has equal length"""
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError(msg[9])

    """checks if matrix multiplication is possible"""
    if len(m_a[0]) != len(m_b):
        raise ValueError(msg[10])

    rows_a = len(m_a)
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])
    result = [[0 for col in range(cols_b)] for row in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
