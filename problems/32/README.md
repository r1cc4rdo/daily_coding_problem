## Problem 32

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.

Example:

    >>> em = [[1, 2, 3], [1./2, 1, 3./2], [1./3, 2./3, 1]]
    >>> coding_problem_32(em)
    True

    >>> em[0][2] = 2.98
    >>> coding_problem_32(em)
    False
