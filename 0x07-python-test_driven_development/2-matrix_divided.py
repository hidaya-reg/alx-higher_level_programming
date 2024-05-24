#!/usr/bin/python3
"""unction that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by `div`

    Args:
        matrix (list of lists): The matrix to be divided.
                            Must contain integers or floats.
        div (int or float): The divisor used for division.
                        Must be a number and cannot be zero

    Returns:
        list of lists: A new matrix with elements divided by `div`
            and rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not list of lists of integers or floats,
               if rows of the matrix have different sizes,
               or if `div` is not a number.
        ZeroDivisionError: If `div` is equal to zero.
    """
    if not all(isinstance(r, list) for r in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    if not all(isinstance(elt, (int, float)) for r in matrix for elt in r):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in r] for r in matrix]
