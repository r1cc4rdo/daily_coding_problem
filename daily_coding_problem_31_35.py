def coding_problem_31():
    """
    The edit distance between two strings refers to the minimum number of character insertions, deletions, and
    substitutions required to change one string to the other. For example, the edit distance between "kitten" and
    "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".
    Given two strings, compute the edit distance between them.

    >>> coding_problem_31()

    """
    pass


def coding_problem_32():
    """
    Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
    possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
    any currency, so that you can end up with some amount greater than A of that currency.
    There are no transaction costs and you can trade fractional quantities.

    >>> coding_problem_32()

    """
    pass


def coding_problem_33():
    """
    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
    the list so far on each new element. Recall that the median of an even-numbered list is the average of the two
    middle numbers.

    For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
    [2, 1.5, 2, 3.5, 2, 2, 2]

    >>> coding_problem_33()

    """
    pass


def coding_problem_34():
    """
    Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
    anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
    lexicographically earliest one (the first one alphabetically).

    For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is
    the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding
    three letters, but "ecarace" comes first alphabetically.

    As another example, given the string "google", you should return "elgoogle".

    >>> coding_problem_34()

    """
    pass


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
