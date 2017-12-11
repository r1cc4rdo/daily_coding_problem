import re


def lc_basic_calculator(s):
    """
    From https://leetcode.com/problems/basic-calculator
    Examples:

    >>> lc_basic_calculator('1 + 1')
    2
    >>> lc_basic_calculator(' 2-1 + 2 ')
    3
    >>> lc_basic_calculator('(1+(4+5+2)-3)+(6+8)')
    23
    >>> lc_basic_calculator('2-(5-6)')
    3
    """
    class Solution(object):
        def calculate(self, s):
            s = s.replace(' ', '')  # no whitespace
            while '(' in s:  # recursively evaluate sub expressions
                tokens_before = s.split('(')
                token_after = tokens_before[-1].split(')')
                value = self.calculate(token_after[0])
                s = '('.join(tokens_before[:-1]) + str(value) + ')'.join(token_after[1:])
                s = s.replace('--', '+')

            addends = re.split('([+-]?\d+)', s)[1::2]
            return sum(map(int, addends))

    return Solution().calculate(s)


def lc_valid_number(x):
    """
    From https://leetcode.com/problems/valid-number

    Validate if a given string is numeric.
    Note: It is intended for the problem statement to be ambiguous.
    You should gather all requirements up front before implementing one.
    Examples:

    >>> lc_valid_number("0")
    True
    >>> lc_valid_number(" 0.1 ")
    True
    >>> lc_valid_number("abc")
    False
    >>> lc_valid_number("1 a")
    False
    >>> lc_valid_number("2e10")
    True
    """
    class Solution(object):
        @staticmethod
        def is_number(s):
            s = s.strip()
            try:
                _ = float(s)
                return True
            except ValueError:
                return False

    return Solution.is_number(x)


def lc_candies(ratings_list):
    """
    From: https://leetcode.com/problems/candy

    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.

    What is the minimum candies you must give?
    Examples:

    >>> lc_candies([0])
    1
    >>> lc_candies([2, 1])
    3
    >>> lc_candies([1, 3, 7, 2, 1, 3, 5, 2, 4])
    17
    """

    class Solution(object):

        def candy(self, ratings):

            candies = [1] * len(ratings)
            for cnt in range(1, len(ratings)):
                if ratings[cnt] > ratings[cnt - 1]:  # left 2 right
                    candies[cnt] = max(candies[cnt], candies[cnt - 1] + 1)

            for cnt in range(-2, -len(ratings) - 1, -1):
                if ratings[cnt] > ratings[cnt + 1]:  # right 2 left
                    candies[cnt] = max(candies[cnt], candies[cnt + 1] + 1)

            return sum(candies)

    return Solution().candy(ratings_list)


def lc_non_decreasing_array(arr):
    """
    From https://leetcode.com/problems/non-decreasing-array

    Given an array with n integers, your task is to check if it could become non-decreasing by modifying at
    most 1 element. We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
    Examples:

    >>> lc_non_decreasing_array([4, 2, 3])
    True
    >>> lc_non_decreasing_array([4, 2, 1])
    False
    """
    class Solution(object):

        def check_possibility(self, nums):

            idx = len(nums)
            for cnt in xrange(0, len(nums) - 1):
                if nums[cnt] > nums[cnt + 1]:
                    idx = cnt
                    break

            for cnt in xrange(idx + 1, len(nums) - 1):
                if nums[cnt] > nums[cnt + 1]:
                    return False

            return idx <= 0 or idx >= len(nums) - 2 or nums[idx - 1] <= nums[idx + 1] or nums[idx] <= nums[idx + 2]

    return Solution().check_possibility(arr)


def lc_reverse_integer(n):
    """
    Given a 32-bit signed integer, reverse digits of an integer. Assume we are dealing with an environment which could
    only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your
    function returns 0 when the reversed integer overflows.
    Examples:

    >>> lc_reverse_integer(123)
    321
    >>> lc_reverse_integer(-123)
    -321
    >>> lc_reverse_integer(120)
    21
    """
    class Solution(object):

        def reverse(self, x):

            neg = x < 0
            if neg:
                x = -x

            result = 0
            while x:
                result = result * 10 + x % 10
                x /= 10

            if result > 2 ** 31:
                return 0

            return -result if neg else result

    return Solution().reverse(n)


def lc_median_sorted_arrays(a, b):  # work in progress
    """
    From: https://leetcode.com/problems/median-of-two-sorted-arrays

    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    Examples:

    >>> lc_median_sorted_arrays([1, 3, 6, 7, 8], [2, 3, 4, 5])
    4.0
    >>> lc_median_sorted_arrays([1, 3], [2])
    2.0
    >>> lc_median_sorted_arrays([1, 2], [3, 4])
    2.5
    """
    if len(a) > len(b):
        a, b = b, a  # a is now the shortest

    step = len(a) / 2 - 1
    idx_a = len(a) / 2  # median of a
    idx_b = len(b) / 2  # median of b
    while True:

        if a[idx_a] <= b[idx_b]:  # increase

            idx_a += step
            idx_b -= step

        else:  # decrease

            idx_a -= step
            idx_b += step

        step /= 2
        if step == 0:
            break

    return a[idx_a]


def lc_count_primes(n):  # work in progress
    """
    From https://leetcode.com/problems/count-primes

    Count the number of prime numbers less than a non-negative number, n.
    Examples:

    >>> lc_count_primes()

    >>> lc_count_primes()

    >>> lc_count_primes()

    """
    import math

    class Solution(object):

        @staticmethod
        def is_prime(n, primes):

            for p in primes:

                if p > math.sqrt(n):
                    break

                if n % p == 0:
                    return False

            return True

        def count_primes(self, n):

            if n <= 2:
                return 0

            primes = [2]
            for x in xrange(3, n, 2):
                if self.is_prime(x, primes):
                    primes.append(x)

            return len(primes)

    return Solution().count_primes(n)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
