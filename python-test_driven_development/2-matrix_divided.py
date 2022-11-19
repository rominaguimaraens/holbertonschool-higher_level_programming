#!/usr/bin/python3
"""Divides matrix """


def matrix_divided(matrix, div):
    """division"""

    biggestMatx = []  # new empty list

    if not isinstance(div, int or float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lenR = len(matrix[0])
    for elems in matrix:
        internMatx = []  # new list for each row
        if lenR != len(elems):
            raise TypeError("Each row of the matrix must have the same size")
        lenR = len(elems)
        for block in elems:
            if type(block) is not int and type(block) is not float:
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
            newBlock = block / div
            internMatx.append(round(newBlock, 2))
        biggestMatx.append(internMatx)

    return biggestMatx
