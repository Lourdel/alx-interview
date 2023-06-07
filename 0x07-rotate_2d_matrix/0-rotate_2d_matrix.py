#!/usr/bin/python3
"""nxn 2D matrix Rotation"""


def rotate_2d_matrix(matrix):
    """Method rotates a matrix by 90 degress"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
