## Problem 20

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
