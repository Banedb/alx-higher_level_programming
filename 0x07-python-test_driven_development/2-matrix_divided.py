#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""

    if type(matrix) is not list or matrix == [] or any(
            type(row) is not list or any(
                type(i) not in (int, float) for i in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    size = len(matrix[0])
    if any(len(row) != size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div, 2) for i in row] for row in matrix]
