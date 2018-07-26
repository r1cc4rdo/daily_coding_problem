def coding_problem_36(tree):
    """
    Given the root to a binary search tree, find the second largest node in the tree.
    Example:

    >>> tree = [9, [4, [1, None, None], [7, [5, None, None], None]], [31, [14, None, None], [82, None, None]]]
    >>> coding_problem_36(tree)
    31

    Note: in a binary search tree, the second largest node is the root of the largest element.
    """
    value, _, right = tree
    parent = value
    while right:
        parent = value
        value, _, right = right
    return parent


def coding_problem_37(s):
    """
    The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
    You may also use a list or array to represent a set. Example:

    >>> sorted([sorted(subset) for subset in coding_problem_37({1, 2, 3})], cmp=lambda a, b: cmp(len(a), len(b)))
    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    """
    power_set = [[]]
    for element in s:
        power_set.extend([[element] + subset for subset in power_set])
    return power_set


def coding_problem_38(n):
    """
    You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
    where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
    column, or diagonal. From this Wikipedia article https://en.wikipedia.org/wiki/Eight_queens_puzzle :

    >>> [coding_problem_38(n + 1) for n in range(8)]
    [1, 0, 0, 2, 10, 4, 40, 92]

    Note: this could be made much faster by passing only valid coordinates instead of all of them each time, but
    it is an exercise left for the reader ;)
    """
    def is_threat(new_queen, board_arrangement):
        for already_placed in board_arrangement:
            if new_queen[0] == already_placed[0] or new_queen[1] == already_placed[1] or \
               abs(new_queen[0] - already_placed[0]) == abs(new_queen[1] - already_placed[1]):
                return True
        return False  # otherwise

    all_coordinates = [(i, j) for i in range(n) for j in range(n)]
    valid_arrangements = {frozenset()}  # set for duplicate removal, empty initial arrangement
    for _ in range(n):
        valid_arrangements = set(arrangement.union([coord]) for arrangement in valid_arrangements
                                 for coord in all_coordinates if not is_threat(coord, arrangement))
    return len(valid_arrangements)


def coding_problem_39():
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

    >>> coding_problem_39()

    """
    pass


def coding_problem_40():
    """
    Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
    find and return the non-duplicated integer. Do this in O(N) time and O(1) space.
    For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

    >>> coding_problem_40()

    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
