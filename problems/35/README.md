##Problem 35

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