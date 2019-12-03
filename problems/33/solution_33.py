from bisect import insort


def coding_problem_33(array):
    """
    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
    the list so far on each new element. Recall that the median of an even-numbered list is the average of the two
    middle numbers. Example:

    >>> coding_problem_33([2, 1, 5, 7, 2, 0, 5])
    [2, 1.5, 2, 3.5, 2, 2.0, 2]
    """
    medians, sorted_partial_array = [], []
    for index, element in enumerate(array):
        insort(sorted_partial_array, element)  # search is O(log(n)) but insertion is O(n)
        median = sorted_partial_array[index // 2]
        if index % 2:
            median = (median + sorted_partial_array[index // 2 + 1]) / 2
        medians.append(median)

    return medians


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
