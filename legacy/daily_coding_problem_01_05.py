from collections import deque


def coding_problem_01(stack):
    """
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using one other queue.
    Example:

    >>> coding_problem_01([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]
    >>> coding_problem_01([1, 2, 3, 4, 5, 6])
    [1, 6, 2, 5, 3, 4]

    Note: with Python lists, you could instead islice(chain.from_iterable(izip(l, reversed(l))), len(l))
    """
    queue = deque([])  # stack S:[1,2,3,4,5], queue Q:[]
    for cnt in range(len(stack) - 1):  # move stack into queue. S:[1], Q:[5,4,3,2]
        queue.append(stack.pop())
    for cnt in range(len(queue) // 2):
        stack.append(queue.popleft())  # S:[1,5], Q:[4,3,2]
        for cnt2 in range(len(queue) - 1):  # rotate last element to front, S:[1,5], Q:[2,4,3]
            queue.append(queue.popleft())
        stack.append(queue.popleft())  # S:[1,5,2], Q:[4,3]
    if queue:
        stack.append(queue.popleft())
    return stack


def coding_problem_02(l):
    """
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one at i.
    Solve it without using division and in O(n).
    Example:

    >>> coding_problem_02([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    """
    forward = [1] * len(l)
    backward = [1] * len(l)
    for idx in range(1, len(l)):

        forward[idx] = forward[idx - 1] * l[idx - 1]
        backward[-idx - 1] = backward[-idx] * l[-idx]

    return [f * b for f, b in zip(forward, backward)]


def coding_problem_03(s):
    """
    Given the root to a binary tree, implement serialize(root), which serializes the tree
    into a string, and deserialize(s), which deserializes the string back into the tree.
    Example:

    >>> s = '3 2 1 None None None 4 5 None None 6 None None'
    >>> de_serialized = coding_problem_03(s)
    >>> re_serialized = de_serialized.serialize_to_string()
    >>> s == re_serialized
    True
    """
    class BinaryNode(object):

        def __init__(self, val, lc=None, rc=None):
            self.val = val
            self.lc = lc
            self.rc = rc

        def serialize(self, queue=None):
            queue = [] if queue is None else queue
            queue.append(self.val)
            if self.val is not None:
                self.lc.serialize(queue)
                self.rc.serialize(queue)
            return queue

        @classmethod
        def deserialize(cls, queue):
            val, lc, rc = queue.pop(), None, None
            if val is not None:
                lc = cls.deserialize(queue)
                rc = cls.deserialize(queue)
            return BinaryNode(val, lc, rc)

        def serialize_to_string(self):
            return ' '.join(repr(element) for element in self.serialize())

        @classmethod
        def deserialize_from_string(cls, s):
            return cls.deserialize([int(token) if token != 'None' else None for token in s.split(' ')][::-1])

    return BinaryNode.deserialize_from_string(s)


def coding_problem_04(array):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    You can modify the input array in-place.
    Example:

    >>> coding_problem_04([3, 4, -1, 1])
    2
    >>> coding_problem_04([1, 2, 0])
    3
    >>> coding_problem_04([4, 1, 2, 2, 2, 1, 0])
    3

    Notes: the code below is a bucket sort variant, and therefore has linear time complexity equal to O(n).
    More in detail, all the for loops in the code are O(n). The while loop is also linear, because it loops
    only when element are not ordered and each iteration correctly positions one element of the array.

    This was my original implementation, which however is not constant space:

        bucket_sort = [True] + [False] * len(arr)  # skip 0 index
        for element in filter(lambda x: 0 < x < len(arr), arr):
            bucket_sort[element] = True
        return bucket_sort.index(False)

    The following one, also not constant space but possibly more understandable,
    has been contributed by NikhilCodes (https://github.com/NikhilCodes):

        arr = set(arr)  # O(n)
        max_val = max(arr)  # O(n)
        missing_val = max_val + 1
        for e in range(1, max_val + 1):  # O(n)
            if e not in arr:  # O(1)
                missing_val = e
                break
        return missing_val
    """
    array.append(0)  # helps by aligning integers with their indexes
    for index, element in enumerate(array):  # remove out of bounds values
        if not (0 < element < len(array)):
            array[index] = 0

    for index in range(len(array)):  # in-place bucket sort
        while True:
            element = array[index]
            if (index == element) or (element == array[element]):  # already in order OR repeated element
                break
            array[index], array[element] = array[element], element  # swap elements

    for index, element in enumerate(array):
        if index != element:  # find the first missing
            return index
    
    return len(array)  # if here, the sought integer is past the array end


def coding_problem_05():
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    Given this implementation of cons below, implement car and cdr.
    Examples: car(cons(3, 4)) == 3, cdr(cons(3, 4)) == 4

    >>> coding_problem_05()
    True
    """
    def cons(a, b):
        return lambda f: f(a, b)

    def car(f):
        return f(lambda a, b: a)

    def cdr(f):
        return f(lambda a, b: b)

    return car(cons(3, 4)) == 3 and cdr(cons(3, 4)) == 4


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
