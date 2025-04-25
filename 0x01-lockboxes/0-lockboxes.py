#!/usr/bin/env python3
"""
determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    boxes: list of lists
    return: true of false
    """
    n = len(boxes)
    visited = set([0])
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if 0 <= key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
