import numpy as np


def coding_problem_32(exchange_matrix):
    """
    Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
    possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
    any currency, so that you can end up with some amount greater than A of that currency.
    There are no transaction costs and you can trade fractional quantities.

    >>> em = [[1, 2, 3], [1./2, 1, 3./2], [1./3, 2./3, 1]]
    >>> coding_problem_32(em)
    True

    >>> em[0][2] = 2.98
    >>> coding_problem_32(em)
    False

    Note: idea is that given a single row in the currency exchange matrix, it is possible to generate the entire 2D
    array. Any difference between the given currency exchange matrix and the computed one implies the possibility of
    arbitration.

    For example, for five currencies and given the exchange rates from the first to the other 4 [b, c, d, e]:

      |  A   B   C   D   E
    --+------------------
    A |  1   b   c   d   e
    B | 1/b  1  c/b d/b e/b
    C | 1/c b/c  1  d/b e/c
    D | 1/d b/d c/d  1  e/d
    E | 1/e b/e c/e d/e  1

    Since floating point quantities are involved, we need to test for approximate equality.
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
