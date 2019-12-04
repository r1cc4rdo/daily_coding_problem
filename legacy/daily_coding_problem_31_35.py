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


def coding_problem_32(exchange_matrix):
    """
    Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
    possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
    any currency, so that you can end up with some amount greater than A of that currency.
    There are no transaction costs and you can trade fractional quantities.

    >>> em = [[1, 2, 3], [1./2, 1, 3./2], [1./3, 2./3, 1]]
    >>> coding_problem_32(em)
    True

    >>> em[0][2] = 2.98
    >>> coding_problem_32(em)
    False

    Note: idea is that given a single row in the currency exchange matrix, it is possible to generate the entire 2D
    array. Any difference between the given currency exchange matrix and the computed one implies the possibility of
    arbitration.

    For example, for five currencies and given the exchange rates from the first to the other 4 [b, c, d, e]:

      |  A   B   C   D   E
    --+------------------
    A |  1   b   c   d   e
    B | 1/b  1  c/b d/b e/b
    C | 1/c b/c  1  d/b e/c
    D | 1/d b/d c/d  1  e/d
    E | 1/e b/e c/e d/e  1

    Since floating point quantities are involved, we need to test for approximate equality.
    """
    em = np.array(exchange_matrix)  # ideally, we should test if the exchange_matrix is well-formed
    cem = np.vstack([em[0, :] / em[0, n] for n in range(len(em))])  # computed exchange_matrix
    return np.allclose(em, cem)


def coding_problem_33(arr):
    """
    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
    the list so far on each new element. Recall that the median of an even-numbered list is the average of the two
    middle numbers. Example:

    >>> coding_problem_33([2, 1, 5, 7, 2, 0, 5])
    [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]

    Note: cheating with numpy below, but I see no reason to make it more complicated given the request. An efficient
    implementation would keep sorted in place the first n elements and do an insertion sort pass each time.
    """
    return [np.median(arr[:n + 1]) for n in range(len(arr))]


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


def coding_problem_35(rgbs):
    """
    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the 'R's
    come first, the 'G's come second, and the 'B's come last. You can only swap elements of the array.
    Do this in linear time and in-place. For example:

    >>> coding_problem_35(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
    ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    The problem can be solved by (insertion) sorting as follows.
    This solution does not take advantage of the expected high number of equal value elements.

    >>> rgbs = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    >>> for i in range(len(rgbs) - 1):
    ...     for j in range(i + 1, len(rgbs)):
    ...         if rgbs[i] < rgbs[j]:  # 'R' > 'G' > 'B'
    ...             rgbs[i], rgbs[j] = rgbs[j], rgbs[i]
    >>> rgbs
    ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    Sorting as described above has a complexity of O(n^2).
    The following solution does at most two passes, and therefore is O(n).
    """
    left_index, right_index = 0, len(rgbs) - 1
    while True:  # move Rs to front

        while rgbs[left_index] == 'R' and left_index < right_index:  # advance to first non R
            left_index += 1

        while rgbs[right_index] != 'R' and left_index < right_index:  # regress to last R
            right_index -= 1

        if left_index >= right_index:
            break

        rgbs[left_index], rgbs[right_index] = rgbs[right_index], rgbs[left_index]

    right_index = len(rgbs) - 1
    while True:  # move Bs to tail

        while rgbs[left_index] != 'B' and left_index < right_index:  # advance to first B
            left_index += 1

        while rgbs[right_index] == 'B' and left_index < right_index:  # regress to last non B
            right_index -= 1

        if left_index >= right_index:
            break

        rgbs[left_index], rgbs[right_index] = rgbs[right_index], rgbs[left_index]

    return rgbs


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
