import operator as ops


def coding_problem_46(str):
    """
    Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum
    length, return any one. Examples:

    >>> coding_problem_46("aabcdcb")
    'bcdcb'
    >>> coding_problem_46("bananas")
    'anana'
    """
    for length in range(len(str), 0, -1):
        for offset in range(len(str) - length + 1):
            sub_str = str[offset:offset + length]
            if sub_str == sub_str[::-1]:
                return sub_str


def coding_problem_47(prices):
    """
    Given a array of numbers representing the stock prices of a company in chronological order, write a function that
    calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you
    can sell it. For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5
    dollars and sell it at 10 dollars.

    >>> coding_problem_47([9, 11, 8, 5, 7, 10])
    5

    Here's the inefficient one-liner:

    >>> prices = [9, 11, 8, 5, 7, 10]
    >>> max([max(prices[today + 1:]) - prices[today] for today in xrange(len(prices) - 1)])
    5
    """
    max_future_price, max_profit = None, None
    for index in range(len(prices) - 1, 0, -1):
        max_future_price = max(max_future_price, prices[index])
        max_profit = max(max_profit, max_future_price - prices[index - 1])
    return max_profit


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


def coding_problem_49(arr):
    """
    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
    42, 14, -5, and 86. Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any
    elements. Do this in O(N) time.
    Examples:

    >>> coding_problem_49([34, -50, 42, 14, -5, 86])
    137
    >>> coding_problem_49([-5, -1, -8, -9])
    0

    Note: this is similar to the stock prices example of #47.

    Note2: alas, I was on the free tier and this is the last problem I was sent. It's been fun, enabling and
    informative. Thank you dailycodingproblem.com !
    """
    cumulative_sum, cumulative_sums = 0, [0]
    for val in arr:
        cumulative_sum += val
        cumulative_sums.append(cumulative_sum)

    highest_peak, max_sum = None, 0
    for index in range(len(cumulative_sums) - 1, 0, -1):
        highest_peak = max(highest_peak, cumulative_sums[index])
        max_sum = max(max_sum, highest_peak - cumulative_sums[index - 1])

    return max_sum


def coding_problem_50(tree_or_number):
    """
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

    Note: problem 49 was the last one I received; this comes from github.com/r1cc4rdo/daily_coding_problem/pull/7,
    a pull request from RMPR (https://github.com/RMPR). Thanks!
    """
    if not isinstance(tree_or_number, tuple):  # it's an integer leaf
        return tree_or_number

    op, left, right = tree_or_number
    op2fun = {'+': ops.add, '-': ops.sub, '*': ops.mul, '/': ops.truediv}
    return op2fun[op](coding_problem_50(left), coding_problem_50(right))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
