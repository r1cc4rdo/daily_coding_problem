import numpy as np


def coding_problem_34(s):
    """
    Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
    anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
    lexicographically earliest one (the first one alphabetically).
    Examples:

    >>> coding_problem_34("race")
    'ecarace'
    >>> coding_problem_34("google")
    'elgoogle'
    >>> coding_problem_34("aibohphobia")
    'aibohphobia'

    Note: this is similar to #31.
    For each given word w, there are 2*len(w)-1 possible palindromes made using as centers either a character (len(w))
    or the location between two characters (len(w)-1).
    """
    def recurse(palindrome, before, after):
        if not before or not after:
            return after[::-1] + before + palindrome + before[::-1] + after

        if before[-1] == after[0]:
            return recurse(after[0] + palindrome + after[0], before[:-1], after[1:])

        from_before = recurse(before[-1] + palindrome + before[-1], before[:-1], after)
        from_after = recurse(after[0] + palindrome + after[0], before, after[1:])
        if len(from_before) == len(from_after):
            return min(from_before, from_after)  # same length, pick lexicographically smaller

        return (from_before, from_after)[len(from_before) > len(from_after)]  # pick shortest

    def pivots(word):
        for index in range(len(word)):
            yield (word[index], word[:index], word[index+1:])
        for index in range(1, len(word)):
            yield ('', word[:index], word[index:])

    candidates = [recurse(palindrome, before, after) for palindrome, before, after in pivots(s)]
    return min(filter(lambda candidate: len(candidate) == min(map(len, candidates)), candidates))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
