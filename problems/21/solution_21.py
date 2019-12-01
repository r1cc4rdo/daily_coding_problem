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
    for event in room_allocation:
        rooms += event  # occupied or released
        max_rooms = max(max_rooms, rooms)
    assert(rooms == 0)

    return max_rooms


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
