import operator as ops


def coding_problem_50(tree_or_number):
    r"""
    Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node
    is one of '+', '-', '*' or '/'. Given the root to such a tree, write a function to evaluate it.
    For example, given the following tree:

         *
       /   \
      +     +
     / \   / \
    3   2 4   5

    you should return 45, as it is (3 + 2) * (4 + 5).
    Examples:

    >>> coding_problem_50(('*', ('+', 3, 2), ('+', 4, 5)))  # (3 + 2) * (4 + 5) == 45
    45
    >>> coding_problem_50(('/', ('+', ('+', 1, 2), 3), 12))  # (1 + 2 + 3) / 12 == 0.5
    0.5
    """
    if not isinstance(tree_or_number, tuple):  # it's an integer leaf
        return tree_or_number

    op, left, right = tree_or_number
    op2fun = {'+': ops.add, '-': ops.sub, '*': ops.mul, '/': ops.truediv}
    return op2fun[op](coding_problem_50(left), coding_problem_50(right))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
