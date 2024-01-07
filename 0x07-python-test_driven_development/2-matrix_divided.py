#!/usr/bin/python3
"""2-matrix_divided
This module contains a single function for dividing all elements of a matrix
Functions:
    matrix_divided(matrix, div): dividided given matrix by given divisor
"""


def matrix_divided(matrix, div):
    """Division of matrix function
    args:
        matrix: matrix to be divided
        div: divisor
    Return: new matrix of dividends
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check if matrix is empty or not a list
    if (not isinstance(matrix, list) or matrix == []
        or not isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        # check if all rows are lists and row is not empty
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        # divide matrix elements by div and add to new_matrix
        new_list = []
        for _ in row:
            if not isinstance(_, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            num = _ / div
            new_list.append(round(num, 2))
            # or new_list.append("{:.2f}".format(num))

        # check if all rows of the matrix have same size
        if len(new_list) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(new_list)

    return new_matrix
