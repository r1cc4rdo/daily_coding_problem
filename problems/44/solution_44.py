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
    """
    sorted_indexes = sorted(range(len(arr)), key=lambda x: arr[x])

    inversions = 0
    while sorted_indexes:
        inversions += sorted_indexes[0]
        sorted_indexes = [si - 1 if si > sorted_indexes[0] else si for si in sorted_indexes[1:]]

    return inversions


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
