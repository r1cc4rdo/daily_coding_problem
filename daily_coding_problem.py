from itertools import chain, izip, islice
import numpy as np


def coding_problem_1(l):
    """
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using one other queue. Example:
    >>> list(coding_problem_1([1, 2, 3, 4, 5]))
    [1, 5, 2, 4, 3]
    """
    return islice(chain.from_iterable(izip(l, reversed(l))), len(l))


def coding_problem_2(l):
    """
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one at i.
    Solve it without using division and in O(n). Example:
    >>> coding_problem_2([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    """
    result = np.ones(len(l), dtype=type(l[0]))
    for idx in xrange(len(l)):
        prev = result[idx]
        result *= l[idx]
        result[idx] = prev
    return list(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
