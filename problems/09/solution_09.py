def coding_problem_09(numbers):
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
    The "largest sum of non-adjacent numbers" is the sum of any subset of non-contiguous elements.
    Solution courtesy of Kye Jiang (https://github.com/Jedshady).
    Examples:

    >>> coding_problem_09([2, 4, 6, 8])
    12
    >>> coding_problem_09([5, 1, 1, 5])
    10
    >>> coding_problem_09([1, 2, 3, 4, 5, 6])
    12
    >>> coding_problem_09([-8, 4, -3, 2, 3, 4])
    10
    >>> coding_problem_09([2, 4, 6, 2, 5])
    13
    """
    if not numbers:
        return 0

    if len(numbers) <= 2:
        return max(numbers)

    with_last = coding_problem_09(numbers[:-2]) + numbers[-1]  # sum include last number
    without_last = coding_problem_09(numbers[:-1])  # sum without last number
    return max(with_last, without_last)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
