import math


def coding_problem_38(n):
    """
    You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
    where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
    column, or diagonal. From this Wikipedia article https://en.wikipedia.org/wiki/Eight_queens_puzzle :

    >>> [coding_problem_38(n + 1) for n in range(7)]
    [1, 0, 0, 2, 10, 4, 40]

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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
