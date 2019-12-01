from collections import deque


def coding_problem_03(s):
    """
    Given the root to a binary tree, implement serialize(root), which serializes the tree
    into a string, and deserialize(s), which deserializes the string back into the tree.
    Example:

    >>> s = '3 2 1 None None None 4 5 None None 6 None None'
    >>> de_serialized = coding_problem_03(s)
    >>> re_serialized = de_serialized.serialize_to_string()
    >>> s == re_serialized
    True
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
