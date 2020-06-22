def coding_problem_30(arr):
    """
    You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
    is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled
    up. Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
    Examples:
    >>> coding_problem_30([])  # no water trapped
    0
    >>> coding_problem_30([1])  # no water trapped
    0
    >>> coding_problem_30([2, 1])  # no water trapped
    0
    >>> coding_problem_30([1, 2, 2, 3, 1, 1])  # no water trapped
    0
    >>> coding_problem_30([2, 1, 2])  # 1@1, 1 unit of water at index 1
    1
    >>> coding_problem_30([3, 0, 1, 3, 0, 5])  # 3@1 2@2 3@4
    8
    >>> coding_problem_30([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 1@2 1@4 2@5 1@6 1@9
    6

    The idea here is to find inner basins bounded by areas of higher elevation.
    Starting from the left and right boundaries, we keep track of the highest value found so far.
    We respectively advance or retreat either end until they collide. We always move the lowest.
    Water gets trapped at a index if its value is lower than both the current left and right maximums.
    The code is equivalent to the following, but more efficient since it required no copies and a single pass:

        def monotonically_increasing(a):
            filled = a[:]
            for index in range(1, len(a)):
                filled[index] = max(filled[index], filled[index - 1])
            return filled

        from_left = monotonically_increasing(arr)
        from_right = monotonically_increasing(arr[::-1])[::-1]
        water = sum(min(l, r) - a for a, l, r in zip(arr, from_left, from_right))
    """
    if len(arr) <= 2:
        return 0

    water = 0
    left_index, left_max_value = 0, arr[0]
    right_index, right_max_value = len(arr) - 1, arr[-1]
    while left_index < right_index:

        advance_left = left_max_value < right_max_value
        left_index += 1 if advance_left else 0
        right_index -= 0 if advance_left else 1

        index = left_index if advance_left else right_index
        water += max(0, min(left_max_value, right_max_value) - arr[index])

        left_max_value = max(left_max_value, arr[left_index])
        right_max_value = max(right_max_value, arr[right_index])

    return water


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
