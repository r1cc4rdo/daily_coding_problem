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
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
