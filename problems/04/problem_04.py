from collections import deque


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
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
