#!/usr/bin/python3
"""
finds the minimum operation
"""


def minOperations(n):
    """
    calculate fewest number of operations
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
