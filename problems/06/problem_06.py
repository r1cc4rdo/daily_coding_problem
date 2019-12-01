def coding_problem_06():
    """
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields, it holds a field named both, which is a XOR of the next node
    and the previous node. Implement a XOR linked list; it has an add(element) which adds the element to the end,
    and a get(index) which returns the node at index.
    Example:

    >>> l = coding_problem_06()
    >>> for cnt in xrange(0, 4):
    ...     l.add(cnt)
    >>> l.get(2) == 2
    True

    Note: python does not have actual pointers (id() exists but it is not an actual pointer in all implementations).
    For this reason, we use a python list to simulate memory. Indexes are the addresses in memory. This has the
    unfortunate consequence that the travel logic needs to reside in the List class rather than the Node one.
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
