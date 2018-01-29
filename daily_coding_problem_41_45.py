def coding_problem_41():
    """
    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a
    starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple
    possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
    starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
    Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
    Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should
    return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
    However, the first one is lexicographically smaller.

    >>> coding_problem_41()

    """
    pass


def coding_problem_42():
    """
    Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
    If such a subset cannot be made, then return null.
    Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

    >>> coding_problem_42()

    """
    pass


def coding_problem_43():
    """
    Implement a stack that has the following methods:

        push(val), which pushes an element onto the stack
        pop(), which pops off and returns the topmost element of the stack.
            If there are no elements in the stack, then it should throw an error or return null.
        max(), which returns the maximum value in the stack currently.
            If there are no elements in the stack, then it should throw an error or return null.

    Each method should run in constant time.

    >>> coding_problem_43()

    """
    pass


def coding_problem_44():
    """
    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
    and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
    You may assume each element in the array is distinct.

    For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and
    (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

    >>> coding_problem_44()

    """
    pass


def coding_problem_45():
    """
    Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
    function rand7() that returns an integer from 1 to 7 (inclusive).

    >>> coding_problem_45()

    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
