#!/usr/bin/python3
""" n queen problem """
import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in queens:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve(n, row=0, queens=[], solutions=[]):
    """Recursive backtracking solver."""
    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(n, row + 1, queens, solutions)
            queens.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
