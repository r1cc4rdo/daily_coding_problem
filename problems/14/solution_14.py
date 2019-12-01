from bisect import bisect_left as bisect
import random


def coding_problem_14():
    """
    The area of a circle is defined as $\pi r^2$. Estimate $\pi$ to 3 decimal places using a Monte Carlo method.
    Example:

    >>> import math
    >>> import random
    >>> random.seed(0xBEEF)
    >>> pi_approx = coding_problem_14()
    >>> abs(math.pi - pi_approx) < 1e-2
    True

    Note: the unit test above is not testing for 3 decimal places, but only 2. Getting to 3 significant digits would
    require too much time each time, since convergence is exponentially slow. Also priming the random number generator
    to avoid random failure for unlucky distributions of samples.
    """
    import math
    import random

    inside = samples = cnt = 0
    pi_approx = 3.0  # physicist $/pi$
    while True:

        for cnt in xrange(10000):

            inside += math.hypot(random.random(), random.random()) <= 1

        samples += cnt + 1
        prev_pi, pi_approx = pi_approx, 4 * float(inside) / samples
        if abs(pi_approx - prev_pi) < 1e-5:
            return pi_approx


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
