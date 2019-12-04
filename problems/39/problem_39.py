def coding_problem_39(cells):
    """
    Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or
    alive, and at each tick, the following rules apply:

        Any live cell with less than two live neighbours dies.
        Any live cell with two or three live neighbours remains living.
        Any live cell with more than three live neighbours dies.
        Any dead cell with exactly three live neighbours becomes a live cell.
        A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

    Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
    and the number of steps it should run for. Once initialized, it should print out the board state at each step.
    Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to
    bottom-rightmost live cell.

    You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
    Example. Simulate a glider https://en.wikipedia.org/wiki/Glider_(Conway%27s_Life) advancing five steps:

    >>> gol = coding_problem_39(((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)))
    >>> for _ in range(5):
    ...     print gol
    ...     gol.simulate()
    ..*
    *.*
    .**
    <BLANKLINE>
    *..
    .**
    **.
    <BLANKLINE>
    .*.
    ..*
    ***
    <BLANKLINE>
    *.*
    .**
    .*.
    <BLANKLINE>
    ..*
    *.*
    .**
    <BLANKLINE>
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
