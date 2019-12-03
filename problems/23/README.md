## Problem 23

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on. Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start. If there is no possible
path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap
around the edges of the board.

Examples:

    >>> map = [[False, False, False, False], [True, True, False, True],
    ...        [False, False, False, False], [False, False, False, False]]
    >>> coding_problem_23(matrix, (3, 0), (0, 0))
    7
    
    >>> map[1][2] = True  # close off path
    >>> coding_problem_23(matrix, (3, 0), (0, 0))  # returns None
    
