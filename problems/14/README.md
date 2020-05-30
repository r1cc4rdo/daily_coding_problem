## [<<](../13) [14] Monte-Carlo estimate of Pi [>>](../15)

The area of a circle is defined as πr². Estimate π to 3 decimal places using a Monte Carlo method.

Example:

    >>> import math
    >>> import random
    >>> random.seed(0xBEEF)
    >>> pi_approx = coding_problem_14()
    >>> abs(math.pi - pi_approx) < 1e-2
    True
