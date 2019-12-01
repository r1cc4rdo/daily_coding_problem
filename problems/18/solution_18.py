def coding_problem_18(arr, k):
    """
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
    sub-array of length k. Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not
    need to store the results. You can simply print them out as you compute them.
    Example:

    >>> coding_problem_18([10, 5, 2, 7, 8, 7], 3)
    [10, 7, 8, 8]
    """
    for cnt in xrange(k - 1):
        arr = [max(value, other) for value, other in zip(arr[:-1], arr[1:])]

    return arr


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
