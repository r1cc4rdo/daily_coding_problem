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
    root_value = po[0]
    root_index = io.index(root_value)
    io_left_nodes = io[:root_index]
    io_right_nodes = io[root_index + 1:]

    po_left_nodes = [val for val in po if val in io_left_nodes]
    po_right_nodes = [val for val in po if val in io_right_nodes]

    left_subtree = coding_problem_48(io_left_nodes, po_left_nodes) if io_left_nodes else None
    right_subtree = coding_problem_48(io_right_nodes, po_right_nodes) if io_right_nodes else None
    return [root_value, left_subtree, right_subtree]


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
