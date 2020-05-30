## [<<](../10) [11] Implement an autocomplete system [>>](../12)

Implement an autocomplete system. That is, given a query string s and a dictionary of all possible query strings,
return all strings in the dictionary that have s as a prefix.

**Hint**: Try pre-processing the dictionary into a more
efficient data structure to speed up queries.

Example:

    >>> words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
    >>> coding_problem_11(words, 'abo')
    ['abode', 'about', 'above']
