## [<<](../22) [23] Solve a maze [>>](../24)[23] Solve a maze./22) [23] Solve a maze [>>](../24)

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on. Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start. If there is no possible
path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap
around the edges of the board.

Examples:

    >>> matrix = [[False] * 4] * 4
    >>> matrix[1] = [True, True, False, True]
    >>> coding_problem_23(matrix, (3, 0), (0, 0))
    7

    >>> matrix[1][2] = True  # close off path
    >>> coding_problem_23(matrix, (3, 0), (0, 0))  # None
