#!/usr/bin/python3
"""
python3 program to generate the pascals triangle
"""


def pascal_triangle(n):
    """
    python function to generate the pascal's triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(triangle[i - 1]) - 1):
            curr = triangle[i - 1]
            tmp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
