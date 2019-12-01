import numpy as np


def coding_problem_31(s, t, debt=0):
    """
    Given two strings, compute the edit distance between them.
    The edit distance between two strings refers to the minimum number of character insertions, deletions, and
    substitutions required to change one string to the other.
    Example:

    >>> coding_problem_31("kitten", "sitting")  # k>>s, e>>i, +g
    3
    >>> coding_problem_31("kitten", "cat")  # k>>c, i>>a, -ten
    5
    >>> coding_problem_31("black", "white")
    5
    >>> coding_problem_31("top", "dog")
    2
    """
    if not s or not t:
        return len(s) + len(t) + debt

    i = coding_problem_31(s, t[1:], debt + 1)  # insertion
    d = coding_problem_31(s[1:], t, debt + 1)  # deletion
    s = coding_problem_31(s[1:], t[1:], debt + (s[0] != t[0]))  # substitution / matching character
    return min(i, d, s)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
