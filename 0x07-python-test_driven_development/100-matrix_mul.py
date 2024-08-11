#!/usr/bin/python3
""" Matrix Multiplication """


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b

    Args:
        m_a (list of lists of int/float): First matrix
        m_b (list of lists of int/float): Second matrix

    Returns:
        list of lists of int/float: The product of m_a and m_b

    Raises:
        TypeError:
            - If m_a or m_b is not a list
            - IF m_a or m_b is not a list of lists
            - If any element of m_a or m_b is not int/float
            - If the rows of m_a or m_b are not all the same size
        ValueError:
            - If m_a or m_b is empty ([] or [[]])
            - If m_a and m_b have incompatible dimensions
    """
    # Verify if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Verify if m_a and m_b list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # verify if any element of m_a or m_b is not int/float
    if not all(isinstance(elt, (int, float)) for row in m_a for elt in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elt, (int, float)) for row in m_b for elt in row):
        raise TypeError("m_b should contain only integers or floats")

    # verify if m_a or m_b is rectangle
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # verify if m_a or m_b is not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # verify if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix Multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product_sum = 0
            for k in range(len(m_b)):
                product_sum += m_a[i][k] * m_b[k][j]
            row.append(product_sum)
        result.append(row)

    return result
