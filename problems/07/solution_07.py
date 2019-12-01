def coding_problem_07(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    Examples:

    >>> coding_problem_07('111')  # possible interpretations: 'aaa', 'ka', 'ak'
    3
    >>> coding_problem_07('2626')  # 'zz', 'zbf', 'bfz', 'bfbf'
    4
    """
    symbols = map(str, range(1, 27))
    if not s:
        return 1

    matches = filter(lambda symbol: s.startswith(symbol), symbols)
    encodings = [coding_problem_07(s[len(m):]) for m in matches]
    return sum(encodings)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
