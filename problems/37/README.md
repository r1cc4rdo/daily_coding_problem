## [<<](../36) Problem 37 [>>](../38)

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
You may also use a list or array to represent a set.

Example:

    >>> sorted([sorted(subset) for subset in coding_problem_37({1, 2, 3})], key=len)
    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
