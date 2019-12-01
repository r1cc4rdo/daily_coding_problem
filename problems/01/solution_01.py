from collections import deque


def coding_problem_01(stack):
    """
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using one other queue.
    Example:

    >>> coding_problem_01([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]
    >>> coding_problem_01([1, 2, 3, 4, 5, 6])
    [1, 6, 2, 5, 3, 4]

    Note: with itertools, you could instead islice(chain.from_iterable(izip(l, reversed(l))), len(l))
    """
    queue = deque([])  # stack S:[1,2,3,4,5], queue Q:[]
    for _ in range(len(stack) - 1):  # move stack into queue. S:[1], Q:[5,4,3,2]
        queue.append(stack.pop())
    for _ in range(len(queue) // 2):
        stack.append(queue.popleft())  # S:[1,5], Q:[4,3,2]
        for __ in range(len(queue) - 1):  # rotate last element to front, S:[1,5], Q:[2,4,3]
            queue.append(queue.popleft())
        stack.append(queue.popleft())  # S:[1,5,2], Q:[4,3]
    if queue:
        stack.append(queue.popleft())
    return stack


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
