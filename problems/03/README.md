## Problem 3

Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.

Example:

    >>> serialize, deserialize = coding_problem_03()
    >>> s = '>>> YOUR OWN TREE ENCODING HERE <<<'
    >>> isinstance(s, str)
    True

    >>> s == serialize(deserialize(s))
    True
