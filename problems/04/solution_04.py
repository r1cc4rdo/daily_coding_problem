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
    only when element are not ordered and each iteration correctly re-positions one element of the array.
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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
