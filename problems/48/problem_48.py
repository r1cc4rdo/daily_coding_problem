def coding_problem_48(io, po):
    """
    Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
    Example:

    >>> def pre_order(tree):
    ...     return [] if tree is None else [tree[0]] + pre_order(tree[1]) + pre_order(tree[2])

    >>> def in_order(tree):
    ...     return [] if tree is None else in_order(tree[1]) + [tree[0]] + in_order(tree[2])

    >>> tree = ['1B', ['2A', None, None], ['3F', ['4D', ['5C', None, None], ['6E', None, None]], ['7G', None, None]]]
    >>> po = pre_order(tree)  # ['1B', '2A', '3F', '4D', '5C', '6E', '7G']
    >>> io = in_order(tree)  # ['2A', '1B', '5C', '4D', '6E', '3F', '7G']
    >>> tree == coding_problem_48(io, po)
    True
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
