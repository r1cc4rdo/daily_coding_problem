import re


def lc_basic_calculator(string):
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

    return Solution().calculate(string)


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

        @staticmethod
        def candy(ratings):

            candies = [1] * len(ratings)
            for cnt in range(1, len(ratings)):
                if ratings[cnt] > ratings[cnt - 1]:  # left 2 right
                    candies[cnt] = max(candies[cnt], candies[cnt - 1] + 1)

            for cnt in range(-2, -len(ratings) - 1, -1):
                if ratings[cnt] > ratings[cnt + 1]:  # right 2 left
                    candies[cnt] = max(candies[cnt], candies[cnt + 1] + 1)

            return sum(candies)

    return Solution.candy(ratings_list)


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

        @staticmethod
        def check_possibility(nums):

            idx = len(nums)
            for cnt in xrange(0, len(nums) - 1):
                if nums[cnt] > nums[cnt + 1]:
                    idx = cnt
                    break

            for cnt in xrange(idx + 1, len(nums) - 1):
                if nums[cnt] > nums[cnt + 1]:
                    return False

            return idx <= 0 or idx >= len(nums) - 2 or nums[idx - 1] <= nums[idx + 1] or nums[idx] <= nums[idx + 2]

    return Solution.check_possibility(arr)


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

        @staticmethod
        def reverse(x):

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

    return Solution.reverse(n)


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


def lc_count_primes(num):  # work in progress
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

    return Solution().count_primes(num)


def lc_virus(playing_field):
    """
    From https://leetcode.com/contest/weekly-contest-63/problems/contain-virus/

    A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.
    The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells
    contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent
    cells, on the shared boundary. Every night, the virus spreads to all neighboring cells in all four directions
    unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the
    affected area (continuous block of infected cells) that threatens the most uninfected cells the following night.
    There will never be a tie. Can you save the day? If so, what is the number of walls required? If not, and the world
    becomes fully infected, return the number of walls used.
    Examples:

    >>> lc_virus([[0,1,0,0,0,0,0,1],
    ...           [0,1,0,0,0,0,0,1],
    ...           [0,0,0,0,0,0,0,1],
    ...           [0,0,0,0,0,0,0,0]])
    10
    >>> lc_virus([[1,1,1],
    ...           [1,0,1],
    ...           [1,1,1]]
    4
    >>> lc_virus([[1,1,1,0,0,0,0,0,0],
    ...           [1,0,1,0,1,1,1,1,1],
    ...           [1,1,1,0,0,0,0,0,0]])
    13

    [[0,1,1,1,1,0,1,1,0,0],
     [0,0,0,0,0,0,1,1,0,0],
     [0,0,0,0,0,1,0,0,0,1],
     [0,0,1,0,0,0,0,1,0,0],
     [1,0,0,0,0,0,1,0,0,0],
     [0,0,1,1,0,1,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,1],
     [0,0,0,0,0,1,1,0,0,0],
     [0,0,0,1,0,1,0,0,0,0],
     [0,0,1,0,0,0,0,0,1,0]]
    """
    class Solution(object):

        def get_coords(self, grid, test_fun):

            result = []
            for row_index in xrange(len(grid)):
                for col_index in xrange(len(grid[row_index])):
                    if test_fun(grid[row_index][col_index]):
                        result.append((row_index, col_index))

            return result

        def neighbours(self, coord_list, potential_neighbours, dedupe=True):

            result = []
            for i in xrange(len(coord_list)):
                for j in xrange(len(potential_neighbours)):
                    diff = [abs(x0 - x1) for x0, x1 in zip(coord_list[i], potential_neighbours[j])]
                    if 0 in diff and 1 in diff:
                        result.append(potential_neighbours[j])

            return list(set(result) - set(coord_list)) if dedupe else result

        def connected_components(self, coords):

            ccs = []
            while True:

                cell, prev_cell = [coords.pop()], None
                while cell != prev_cell:
                    prev_cell = list(cell)  # copy
                    cell = cell + self.neighbours(cell, coords)

                ccs.append(cell)
                coords = list(set(coords) - set(cell))
                if not coords:
                    break

            return ccs

        def label_virus_zones(self, grid):

            virus = self.get_coords(grid, lambda x: x > 0)
            if virus:
                for idx, cc in enumerate(self.connected_components(virus)):
                    for coord in cc:
                        grid[coord[0]][coord[1]] = idx + 1

            return grid

        def contain_virus(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            from itertools import combinations

            walls = 0
            while True:

                grid = self.label_virus_zones(grid)
                virus_zones = list(set([val for row in grid for val in row if val > 0]))

                virus_spread = []
                uncontaminated = self.get_coords(grid, lambda x: x == 0)

                for zone in virus_zones:
                    zone_coords = self.get_coords(grid, lambda x: x == zone)
                    virus_spread.append(self.neighbours(zone_coords, uncontaminated))

                lost_anyway = []
                for spread1, spread2 in combinations(virus_spread, 2):
                    in_common = set(spread1).intersection(set(spread2))
                    lost_anyway.extend(in_common)

                lost_anyway = set(lost_anyway)
                for index in xrange(len(virus_spread)):
                    virus_spread[index] = list(set(virus_spread[index]) - lost_anyway)

                impacts = [len(spread) for spread in virus_spread]
                if not impacts:
                        break  # done here

                biggest_impact = max(impacts)
                zone_to_contain_id = virus_zones[impacts.index(biggest_impact)]
                zone_to_contain = self.get_coords(grid, lambda x: x == zone_to_contain_id)
                for r, c in zone_to_contain:
                    grid[r][c] = -zone_to_contain_id

                walls += len(self.neighbours(zone_to_contain, uncontaminated, dedupe=False))

                for r, c in lost_anyway:
                    grid[r][c] = 1

                virus_spread.remove(virus_spread[impacts.index(biggest_impact)])
                for spread in virus_spread:
                    for r, c in spread:
                        grid[r][c] = 1

            return walls

    return Solution().containVirus(playing_field)


if __name__ == '__main__':

    playing_field = [[0,1,1,1,1,0,1,1,0,0],
                     [0,0,0,0,0,0,1,1,0,0],
                     [0,0,0,0,0,1,0,0,0,1],
                     [0,0,1,0,0,0,0,1,0,0],
                     [1,0,0,0,0,0,1,0,0,0],
                     [0,0,1,1,0,1,0,0,1,0],
                     [0,0,0,0,0,0,0,0,0,1],
                     [0,0,0,0,0,1,1,0,0,0],
                     [0,0,0,1,0,1,0,0,0,0],
                     [0,0,1,0,0,0,0,0,1,0]]

    print lc_virus(playing_field)

    import doctest
    doctest.testmod(verbose=True)
