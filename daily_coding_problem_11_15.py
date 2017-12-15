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
    def binary_search(list_like, item, mode='any', fmap=None):
        """
        Pretty pleased with this binary search function. Supports searching for the first, last or any match of
        the given item. Both the elements of the list and the item can be optionally mapped through a function which
        should output objects supporting the standard ordering operators <=>.
        """
        fmap = fmap if fmap else lambda x: x
        fitem = fmap(item)

        first = 0
        last = len(list_like) - 1
        while first < last:

            midpoint = (first + last) // 2
            if fmap(list_like[midpoint]) == fitem:

                if mode == 'first':  # continue searching for the first occurrence of item

                    last = midpoint

                elif mode == 'last':  # continue searching for the last occurrence of item

                    if midpoint == first:  # end game

                        if fmap(list_like[last]) == fitem:

                            first += 1

                        else:

                            last -= 1

                    else:  # more than 1 item apart

                        first = midpoint

                else:  # return the index of any occurrence of item

                    return midpoint

            elif fitem < fmap(list_like[midpoint]):

                last = midpoint - 1

            else:

                first = midpoint + 1

        return first if fmap(list_like[first]) == fitem else -1

    strings = [s.lower() for s in sorted(strings)]
    s = binary_search(strings, prefix, 'first', fmap=lambda s: s[:min(3, len(s))])
    e = binary_search(strings, prefix, 'last', fmap=lambda s: s[:min(3, len(s))])
    return strings[s:(e+1)]


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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
