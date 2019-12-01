import numpy as np


def coding_problem_35(rgbs):
    """
    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the 'R's
    come first, the 'G's come second, and the 'B's come last. You can only swap elements of the array.
    Do this in linear time and in-place. For example:

    >>> coding_problem_35(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
    ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    The problem can be solved by (insertion) sorting as follows.
    This solution does not take advantage of the expected high number of equal value elements.

    >>> rgbs = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    >>> for i in range(len(rgbs) - 1):
    ...     for j in range(i + 1, len(rgbs)):
    ...         if rgbs[i] < rgbs[j]:  # 'R' > 'G' > 'B'
    ...             rgbs[i], rgbs[j] = rgbs[j], rgbs[i]
    >>> rgbs
    ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    Sorting as described above has a complexity of O(n^2).
    The following solution does at most two passes, and therefore is O(n).
    """
    left_index, right_index = 0, len(rgbs) - 1
    while True:  # move Rs to front

        while rgbs[left_index] == 'R' and left_index < right_index:  # advance to first non R
            left_index += 1

        while rgbs[right_index] != 'R' and left_index < right_index:  # regress to last R
            right_index -= 1

        if left_index >= right_index:
            break

        rgbs[left_index], rgbs[right_index] = rgbs[right_index], rgbs[left_index]

    right_index = len(rgbs) - 1
    while True:  # move Bs to tail

        while rgbs[left_index] != 'B' and left_index < right_index:  # advance to first B
            left_index += 1

        while rgbs[right_index] == 'B' and left_index < right_index:  # regress to last non B
            right_index -= 1

        if left_index >= right_index:
            break

        rgbs[left_index], rgbs[right_index] = rgbs[right_index], rgbs[left_index]

    return rgbs


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)