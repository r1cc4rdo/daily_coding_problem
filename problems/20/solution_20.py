def coding_problem_20(list_a, list_b):
    """
    Given two singly linked lists that intersect at some point, find the intersecting node.
    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
    For example, given A = 3 -> 7 -> 8 -> 10 -> 1 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
    Example:

    >>> class LinkedListNode(object):
    ...
    ...     def __init__(self, value, child=None):
    ...         self.value = value
    ...         self.next = child
    ...
    ...     def add(self, value):
    ...         return LinkedListNode(value, self)
    ...
    ...     @classmethod
    ...     def len(cls, node):
    ...         count = 0
    ...         while node:
    ...             node = node.next
    ...             count += 1
    ...         return count

    >>> common_tail = LinkedListNode(1).add(10).add(8)
    >>> list_a = LinkedListNode(7, common_tail).add(3)
    >>> list_b = LinkedListNode(1, common_tail).add(99).add(14)
    >>> coding_problem_20(list_a, list_b)
    8

    Note: the problem statement above is ambiguous and misleading. I think B list was originally supposed to end
    up with a -> 1. This is how most problems of this type I googled are formulated. If this is not the case, this
    is akin to finding the longest common list between the lists, which I believe cannot be solved in O(M+N).
    """
    len_a = list_a.len(list_a)
    len_b = list_b.len(list_b)
    if len_b > len_a:
        list_a, list_b = list_b, list_a

    for advance in range(abs(len_a - len_b)):
        list_a = list_a.next

    for check in range(len_b):
        if list_a is list_b:
            return list_a.value

        list_a = list_a.next
        list_b = list_b.next

    return None


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
