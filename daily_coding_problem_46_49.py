def coding_problem_46():
    """
    Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum
    length, return any one. For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest
    palindromic substring of "bananas" is "anana".

    >>> coding_problem_46()

    """
    pass


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


def coding_problem_48():
    """
    Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

    >>> coding_problem_48()

    """
    pass


def coding_problem_49(arr):
    """
    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
    42, 14, -5, and 86. Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any
    elements.
    Do this in O(N) time.

    >>> coding_problem_49([34, -50, 42, 14, -5, 86])
    137

    >>> coding_problem_49([-5, -1, -8, -9])
    0

    Note: this is similar to the stock prices example of #47.
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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
