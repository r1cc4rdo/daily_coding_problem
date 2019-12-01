from typing import Iterable


def coding_problem_03():
    """
    Given the root to a binary tree, implement serialize(root), which serializes the tree
    into a string, and deserialize(s), which de-serializes the string back into the tree.
    Example:

    >>> serialize, deserialize = coding_problem_03()
    >>> s = '3 2 1 None None None 4 5 None None 6 None None'
    >>> tree = (3, (2, (1, None, None), None), (4, (5, None, None), (6, None, None)))
    >>> isinstance(s, str)
    True

    >>> deserialized = deserialize(s)
    >>> tree == deserialized
    True

    >>> s == serialize(deserialized)
    True

    Notes: the implementation below tries to solve the problem as intended.
    However, one could instead: serialize, deserialize = lambda tree: repr(tree), lambda s: eval(s)
    """
    def deserialize_array(array):
        val = array.pop()
        return None if val is None else (val, deserialize_array(array), deserialize_array(array))

    def flatten(array):
        return [y for x in array for y in flatten(x)] if isinstance(array, Iterable) else [array]

    def serialize(array):
        return ' '.join(repr(element) for element in flatten(array))

    def deserialize(s):
        values = [int(token) if token != 'None' else None for token in s.split()]
        return deserialize_array(values[::-1])

    return serialize, deserialize


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
