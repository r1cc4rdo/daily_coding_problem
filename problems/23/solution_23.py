def coding_problem_23(matrix, start, end):
    """
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

    """
    walkable = {(r, c) for r, row in enumerate(matrix) for c, is_wall in enumerate(row) if not is_wall}
    steps, to_visit = 0, {start}
    while to_visit:
        steps += 1
        walkable -= to_visit
        to_visit = {(nr, nc) for r, c in to_visit for nr, nc in walkable if abs(r - nr) + abs(c - nc) == 1}
        if end in to_visit:
            return steps
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
