def coding_problem_06():
    """
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields, it holds a field named both, which is a XOR of the next node
    and the previous node. Implement a XOR linked list; it has an add(element) which adds the element to the end,
    and a get(index) which returns the node at index.
    Example:

    >>> xll = coding_problem_06()
    >>> for cnt in range(0, 4):
    ...     xll.add(cnt)
    >>> xll.get(2) == 2
    True
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
