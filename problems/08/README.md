##Problem 8

A unival tree (which stands for "universal value") is a tree where all nodes have the same value.
Given the root to a binary tree, count the number of unival subtrees.
Example:

    >>> btree = (0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))
    >>> coding_problem_08(btree)[0]
    6