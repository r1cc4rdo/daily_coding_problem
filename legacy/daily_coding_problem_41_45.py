from copy import copy


def coding_problem_41(flights_db, starting_airport):
    """
    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a
    starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple
    possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    Examples:

    >>> coding_problem_41([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    >>> coding_problem_41([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')  # returns None

    >>> coding_problem_41([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
    ['A', 'B', 'C', 'A', 'C']

    The itinerary ['A', 'C', 'A', 'B', 'C'] is also a valid however the first one is lexicographically smaller.
    """
    if not flights_db:
        return [starting_airport]

    legs = [leg for leg in flights_db if leg[0] == starting_airport]
    for leg in sorted(legs, key=lambda x: x[1]):

        unused_legs = copy(flights_db)
        unused_legs.remove(leg)
        partial_itinerary = coding_problem_41(unused_legs, leg[1])
        if partial_itinerary is not None:
            return [starting_airport] + partial_itinerary

    return None


def coding_problem_42(numbers, target):
    """
    Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
    If such a subset cannot be made, then return null.
    Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    Example:

    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 24)
    [12, 9, 2, 1]
    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 25)  # return None

    >>> coding_problem_42([12, 1, 61, 5, 9, 2], 19)
    [12, 5, 2]
    """
    if target == 0:
        return []

    valid_numbers = [n for n in numbers if 0 < n <= target]
    for number in sorted(valid_numbers, reverse=True):

        remaining_numbers = copy(valid_numbers)
        remaining_numbers.remove(number)
        partial_sum = coding_problem_42(remaining_numbers, target - number)
        if partial_sum is not None:
            return [number] + partial_sum

    return None


def coding_problem_43():
    """
    Implement a stack that has the following methods:

        push(val), which pushes an element onto the stack
        pop(), which pops off and returns the topmost element of the stack.
            If there are no elements in the stack, then it should throw an error or return null.
        max(), which returns the maximum value in the stack currently.
            If there are no elements in the stack, then it should throw an error or return null.

    Each method should run in constant time.

    >>> max_stack = coding_problem_43()
    >>> max_stack.push(1)
    >>> max_stack.max()
    1
    >>> max_stack.push(3)
    >>> max_stack.max()
    3
    >>> max_stack.push(2)
    >>> max_stack.max()
    3
    >>> max_stack.pop()
    2
    >>> max_stack.max()
    3
    >>> _ = max_stack.pop()
    >>> max_stack.max()
    1
    >>> _ = max_stack.pop()
    >>> max_stack.max()
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    >>> _ = max_stack.pop()
    Traceback (most recent call last):
    ...
    IndexError: pop from empty list
    """
    class MaxStack(object):

        def __init__(self):
            self.val_list = []
            self.max_list = []

        def push(self, val):
            self.val_list.append(val)
            self.max_list.append(max(val, self.max()) if self.max_list else val)

        def pop(self):
            self.max_list.pop()
            return self.val_list.pop()

        def max(self):
            return self.max_list[-1]

    return MaxStack()


def coding_problem_44(arr):
    """
    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
    and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
    You may assume each element in the array is distinct.
    Examples:

    >>> coding_problem_44([1, 2, 3, 4, 5])
    0
    >>> coding_problem_44([2, 4, 1, 3, 5])  # inversions: (2, 1), (4, 1), (4, 3)
    3
    >>> coding_problem_44([5, 4, 3, 2, 1])  # every distinct pair forms an inversion
    10

    Note: complexity is that of sorting O(n log(n)) plus a linear pass O(n), therefore bounded by O(n log(n))
    Note2: [TODO] idea is here, but should avoid using .index(), which is a linear search. Committing as is for now.
    """
    inversions = 0
    sorted_indexes = sorted(range(len(arr)), key=lambda x: arr[x])
    for index in range(len(sorted_indexes)):

        destination = sorted_indexes.index(index)
        sorted_indexes.remove(index)
        inversions += destination

    return inversions


def coding_problem_45(rand5):
    """
    Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
    function rand7() that returns an integer from 1 to 7 (inclusive).

    Note: for n >= 24, rand5() ** n is a multiple of 7 and therefore rand5() ** 24 % 7 is an unbiased implementation
    of rand7(). To avoid having to rely on big integer libraries, we use the property (a + b) % n == ((a % n) + b) % n
    which is easy to prove by decomposing a into a // n * n + a % n.

    >>> from random import randint
    >>> rand5 = lambda: randint(0, 4)
    >>> rand7 = coding_problem_45(rand5)
    >>> 0 <= rand7 < 7
    True
    """
    rand7 = 0
    for _ in range(24):
        rand7 = (rand7 * 5 + rand5()) % 7
    return rand7


if __name__ == '__main__':

   import doctest
   doctest.testmod(verbose=True)
