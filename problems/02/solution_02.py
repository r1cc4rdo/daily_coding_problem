def coding_problem_02(l):
    """
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one at i.
    Solve it without using division and in O(n).
    Example:

    >>> coding_problem_02([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    """
    forward = [1] * len(l)
    backward = [1] * len(l)
    for idx in range(1, len(l)):

        forward[idx] = forward[idx - 1] * l[idx - 1]
        backward[-idx - 1] = backward[-idx] * l[-idx]

    return [f * b for f, b in zip(forward, backward)]


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
