from bisect import bisect_left as bisect


def coding_problem_11(strings, prefix):
    """
    Implement an autocomplete system. That is, given a query string s and a dictionary of all possible query strings,
    return all strings in the dictionary that have s as a prefix. Hint: Try pre-processing the dictionary into a more
    efficient data structure to speed up queries.
    Example:

    >>> words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
    >>> coding_problem_11(words, 'abo')
    ['abode', 'about', 'above']

    Note: the complexity of the code below is already logarithmic. Faster speed are possible with hierarchical
    dictionaries or hashing scheme, if we are willing to pay a space complexity trade-off. Using more sophisticated
    approaches must be justified over actual requirements, overkill here.
    """
    dictionary = [s.lower() for s in sorted(strings)]
    next_prefix = prefix + 'a' if prefix[-1] == 'z' else prefix[:-1] + chr(ord(prefix[-1]) + 1)
    return dictionary[bisect(dictionary, prefix):bisect(dictionary, next_prefix)]


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
