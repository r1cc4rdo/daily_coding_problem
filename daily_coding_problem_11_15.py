from bisect import bisect_left as bisect
import random


def coding_problem_11(strings, prefix):
    """
    Implement an autocomplete system. That is, given a query string s and a dictionary of all possible query strings,
    return all strings in the dictionary that have s as a prefix. Hint: Try pre-processing the dictionary into a more
    efficient data structure to speed up queries.
    Example:

    >>> words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
    >>> coding_problem_11(words, 'abo')
    ['abode', 'about', 'above']

    Note: I have been thinking of lots of potential data structures, like hierarchical dictionaries, or hashing.
    Unless otherwise specified, I think space/computation trade-off is not worth doing more than I do below.
    The necessity of using more sophisticated solutions depends on the problem to be solved, overkill here.
    """
    dictionary = [s.lower() for s in sorted(strings)]
    next_prefix = prefix + 'a' if prefix[-1] == 'z' else prefix[:-1] + chr(ord(prefix[-1]) + 1)
    return dictionary[bisect(dictionary, prefix):bisect(dictionary, next_prefix)]


def coding_problem_12(budget, choices):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a
    function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
    integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    Example:

    >>> coding_problem_12(4, [1, 2])
    5
    """
    if budget == 0:
        return 1  # leaf case

    available_choices = [c for c in choices if c <= budget]
    if not available_choices:
        return 0  # unfeasible

    count = 0
    for c in available_choices:
        count += coding_problem_12(budget - c, choices)

    return count


def coding_problem_13(s, k):
    """
    Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
    characters.
    Example:

    >>> coding_problem_13('abcba', 2)  # longest substring with at most 2 distinct characters is 'bcb'
    3
    >>> coding_problem_13('edabccccdccba', 3)  # 'bccccdccb'
    9
    """
    assert(len(s) >= k)

    start_index, end_index, max_length = 0, k, k
    while end_index < len(s):

        end_index += 1
        while True:

            distinct_characters = len(set(s[start_index:end_index]))
            if distinct_characters <= k:
                break

            start_index += 1

        max_length = max(max_length, end_index - start_index)

    return max_length


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


def coding_problem_15(sample_generator):
    """
    Given a stream of elements too large to store in memory, pick a random element from the stream with
    uniform probability.
    Example:

    >>> import random
    >>> random.seed(0xBADC0FFE)
    >>>
    >>> def sample_gen_fun(n):
    ...     for x in xrange(n):
    ...         yield x
    >>>
    >>> num = 10
    >>> hist = [0] * num
    >>> for trials in xrange(5000):
    ...
    ...     hist[coding_problem_15(sample_gen_fun(num))] += 1
    >>>
    >>> all(abs(float(h) / sum(hist) - 1.0 / len(hist)) < 0.01 for h in hist)
    True

    Note: this problem only makes sense if you don't know the total number in advance. Otherwise, you would pick a
    random integer between [0..len[ and record the element corresponding to that index when processed. Setting a seed
    for the random number generator to avoid random failures due to unlucky distributions of samples.

    Strategy: assuming that at round n we have already selected between the available samples with uniform
    probability, accept the incoming one as the new selected sample with a probability that keeps everyone's chances
    fair. Example: at n==1, the first sample as 100% chance of being selected. n==2, second sample 50% chance, n==3
    1/3 chance etc. Proof: for n==5, the prob. of choosing first sample is 1 * 0.5 * 0.666.. * 0.75 * 0.8 = 0.2 = 1/5
    """
    sample_count = 0
    selected_sample = None
    for sample in sample_generator:

        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample

    return selected_sample


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
