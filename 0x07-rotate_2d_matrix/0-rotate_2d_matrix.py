#!/usr/bin/python3
"""
contains rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates an n x n 2d matrix by 90 degrees
    clockwise
                Args:
                        matrix(List(List)): matrix to rotate
                Returns:
                        None;
    """
    # matrix = [[matrix[i][j] for i in range(len(matrix))]
    # for j in range(len(matrix[0]))]
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for m in matrix:
        m.reverse()
    return
