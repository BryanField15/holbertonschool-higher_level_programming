#!/usr/bin/python3
"""
Module containing one function to divide a matrix by a given integer
"""


def matrix_divided(matrix, div):
    """
    Simple function to divide a matrix by a given integer

    Args:
        matrix: matrix of integers or floats
        div: int or float that each element in the matrix will be divided by

    Return:
        a new matrix of quotients rounded to 2dp
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    first_row_size = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
