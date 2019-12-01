import math


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
    Example: simulate a glider (https://en.wikipedia.org/wiki/Glider_(Conway%27s_Life)) advancing one step.

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
    class GameOfLife(object):

        def __init__(self, cells):
            self.displacements = tuple((xd, yd) for yd in [-1, 0, 1] for xd in [-1, 0, 1] if xd != 0 or yd != 0)
            self.cells = set(cells)

        def __str__(self):
            xmin, xmax, ymin, ymax = [min_max(xy) for xy in zip(*self.cells) for min_max in [min, max]]
            return ''.join(('*' if (x, y) in self.cells else '.') + ('\n' if x == xmax else '')
                           for y in range(ymin, ymax + 1) for x in range(xmin, xmax + 1))

        def alive_next_round(self, x, y):
            neighbour_count = sum(1 if (x + xd, y + yd) in self.cells else 0 for xd, yd in self.displacements)
            return neighbour_count == 3 or ((x, y) in self.cells and neighbour_count == 2)

        def simulate(self, steps=1):
            for _ in range(steps):
                active_cells = set((x + xd, y + yd) for x, y in self.cells for xd in [-1, 0, 1] for yd in [-1, 0, 1])
                self.cells = set((x, y) for x, y in active_cells if self.alive_next_round(x, y))

    return GameOfLife(cells)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
