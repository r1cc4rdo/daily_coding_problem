from collections import deque


def coding_problem_03(s):
    """
    Given the root to a binary tree, implement serialize(root), which serializes the tree
    into a string, and deserialize(s), which deserializes the string back into the tree.
    Example:

    >>> s = '3 2 1 None None None 4 5 None None 6 None None'
    >>> de_serialized = coding_problem_03(s)
    >>> re_serialized = de_serialized.serialize_to_string()
    >>> s == re_serialized
    True
    """
    class BinaryNode(object):

        def __init__(self, val, lc=None, rc=None):
            self.val = val
            self.lc = lc
            self.rc = rc

        def serialize(self, queue=None):
            queue = [] if queue is None else queue
            queue.append(self.val)
            if self.val is not None:
                self.lc.serialize(queue)
                self.rc.serialize(queue)
            return queue

        @classmethod
        def deserialize(cls, queue):
            val, lc, rc = queue.pop(), None, None
            if val is not None:
                lc = cls.deserialize(queue)
                rc = cls.deserialize(queue)
            return BinaryNode(val, lc, rc)

        def serialize_to_string(self):
            return ' '.join(repr(element) for element in self.serialize())

        @classmethod
        def deserialize_from_string(cls, s):
            return cls.deserialize([int(token) if token != 'None' else None for token in s.split(' ')][::-1])

    return BinaryNode.deserialize_from_string(s)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
