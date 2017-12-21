def coding_problem_21(times):
    """
    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
    find the minimum number of rooms required.
    Example:

    >>> coding_problem_21([(30, 75), (0, 50), (60, 150)])
    2
    """
    start_times = [(t[0], 1) for t in times]  # [(30, 1), (0, 1), (60, 1)]
    end_times = [(t[1], -1) for t in times]  # [(75, -1), (50, -1), (150, -1)]
    room_allocation = [t[1] for t in sorted(start_times + end_times, key=lambda t: t[0])]  # [1, 1, -1, 1, -1, -1]

    rooms, max_rooms = 0, 0
    for r in room_allocation:
        rooms += r
        max_rooms = max(max_rooms, rooms)
    assert(rooms == 0)

    return max_rooms


def coding_problem_22():
    """

    >>> coding_problem_22()

    """
    pass


def coding_problem_23():
    """

    >>> coding_problem_23()

    """
    pass


def coding_problem_24():
    """

    >>> coding_problem_24()

    """
    pass


def coding_problem_25():
    """

    >>> coding_problem_25()

    """
    pass


if __name__ == '__main__':

    coding_problem_21([(30, 75), (0, 50), (60, 150)])

    import doctest
    doctest.testmod(verbose=True)
