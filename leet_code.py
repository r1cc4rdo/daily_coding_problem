import numpy as np
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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
