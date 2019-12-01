from bisect import bisect_left as bisect
import random


def coding_problem_12(budget, choices):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a
    function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
    integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    Example:

    >>> coding_problem_12(4, [1, 2])
    5
    """
    if budget == 0:
        return 1  # leaf case

    available_choices = [c for c in choices if c <= budget]
    if not available_choices:
        return 0  # unfeasible

    count = 0
    for c in available_choices:
        count += coding_problem_12(budget - c, choices)

    return count


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
