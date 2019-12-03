def coding_problem_30(arr):
    """
    You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
    is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled
    up. Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
    Examples:

    >>> coding_problem_30([2, 1, 2])  # 1@1, 1 unit of water at index 1
    1
    >>> coding_problem_30([3, 0, 1, 3, 0, 5])  # 3@1 2@2 3@4
    8
    >>> coding_problem_30([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 1@2 1@4 2@5 1@6 1@9
    6
    """
    water = 0
    while len(arr) > 2:

        lval = arr[0]  # the idea is: from the smallest left/right boundary, accumulate water level until reaching a
        rval = arr[-1]  # higher wall inside. Then recurse with with the new bound, until only two array entries.
        if lval <= rval:

            cnt = 1
            while arr[cnt] < arr[0]:
                water += arr[0] - arr[cnt]
                cnt += 1

            arr = arr[cnt:]

        else:

            cnt = -2
            while arr[cnt] < arr[-1]:
                water += arr[-1] - arr[cnt]
                cnt -= 1

            arr = arr[:cnt+1]

    return water


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
