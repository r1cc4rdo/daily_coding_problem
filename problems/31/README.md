##Problem 31

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