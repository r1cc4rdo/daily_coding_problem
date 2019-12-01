import operator as ops


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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
