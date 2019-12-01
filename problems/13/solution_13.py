from bisect import bisect_left as bisect
import random


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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
