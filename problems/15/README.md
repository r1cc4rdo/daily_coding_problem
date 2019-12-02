## Problem 15

Given a stream of elements too large to store in memory, pick a random element from the stream with
uniform probability.

Example:

    >>> import random
    >>> random.seed(0xBADC0FFE)

    >>> def sample_gen_fun(n):
    ...     for x in xrange(n):
    ...         yield x

    >>> num = 10
    >>> hist = [0] * num
    >>> for trials in xrange(5000):
    ...     hist[coding_problem_15(sample_gen_fun(num))] += 1

    >>> all(abs(float(h) / sum(hist) - 1.0 / len(hist)) < 0.01 for h in hist)
    True
