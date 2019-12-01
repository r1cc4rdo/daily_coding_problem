import operator as ops


def coding_problem_46(str):
    """
    Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum
    length, return any one. Examples:

    >>> coding_problem_46("aabcdcb")
    'bcdcb'
    >>> coding_problem_46("bananas")
    'anana'
    """
    for length in range(len(str), 0, -1):
        for offset in range(len(str) - length + 1):
            sub_str = str[offset:offset + length]
            if sub_str == sub_str[::-1]:
                return sub_str


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
