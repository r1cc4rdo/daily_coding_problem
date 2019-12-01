import math


def coding_problem_40(numbers):
    """
    Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
    find and return the non-duplicated integer. Do this in O(N) time and O(1) space.
    Examples:

    >>> coding_problem_40([6, 1, 3, 3, 3, 6, 6])
    1
    >>> coding_problem_40([13, 19, 13, 13])
    19

    Note: the code below fails for negative numbers, but you could shift the entire array by the minimum.
    Note2: the implementation below makes it evident that the space complexity is O(log_2(n)) rather than O(1).
    This is always the case, unless a specific integer type or a maximum value are specified (they are not above).
    """
    bits = [0] * int(math.ceil(math.log(max(numbers), 2)))  # low endian
    for number in numbers:
        index = 0
        while number > 0:
            bits[index] += number & 1
            number //= 2
            index += 1
    return sum((b % 3) * 2**i for i, b in enumerate(bits))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)