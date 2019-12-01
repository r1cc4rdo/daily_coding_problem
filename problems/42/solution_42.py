from copy import copy


def coding_problem_42(numbers, target):
    """
    Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
    If such a subset cannot be made, then return null.
    Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    Example:

    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 24)
    [12, 9, 2, 1]
    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 25)  # return None

    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 19)
    [12, 5, 2]
    """
    if target == 0:
        return []

    valid_numbers = [n for n in numbers if 0 < n <= target]
    for number in sorted(valid_numbers, reverse=True):

        remaining_numbers = copy(valid_numbers)
        remaining_numbers.remove(number)
        partial_sum = coding_problem_42(remaining_numbers, target - number)
        if partial_sum is not None:
            return [number] + partial_sum

    return None


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
