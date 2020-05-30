## [<<](../43) [44] Determine how "out of order" an array A is [>>](../45)

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
