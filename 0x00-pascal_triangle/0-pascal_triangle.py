#!/usr/bin/python3
"""
Function to return list of lists representing the pascal triangle
"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    if n <= 0:
        return []
    triangle = []

    for x in range(n):
        row = [1]
        if x > 0:
            last_row = triangle[-1]
            for y in range(1, x):
                row.append(last_row[y-1] + last_row[y])
            row.append(1)

        triangle.append(row)

    return triangle
