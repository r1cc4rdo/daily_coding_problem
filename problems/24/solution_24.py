def coding_problem_24():
    r"""
    Implement locking in a binary tree. A binary tree node can be locked or unlocked only if any of its descendants or
    ancestors are not locked. Write a binary tree node class with the following methods:

        is_locked, which returns whether the node is locked
        lock, which attempts to lock the node. If it cannot be locked, then it should return false.
            Otherwise, it should lock it and return true.
        unlock, which unlocks the node

    You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
    Each method should run in O(h), where h is the height of the tree.

    Example:

    >>> node_class = coding_problem_24()

          root
        /     \
       Y      Z
      / \    / \
     *  *   X  *
           / \
          *  *

    >>> X, Y = node_class(), node_class()
    >>> Z = node_class(right_child=X)
    >>> root = node_class(left_child=Y, right_child=Z)

    >>> Z.lock()
    True

    >>> Z.is_locked()
    True

    >>> root.is_locked()
    False

    >>> root.lock()  # because descendants are locked
    False

    >>> X.lock()  # because ancestors are locked
    False

    >>> Z.unlock()
    True

    >>> X.lock()
    True
    """
    class LockingBinaryTreeNode(object):

        def __init__(self, parent_node=None, left_child=None, right_child=None):
            self.parent, self.left, self.right = parent_node, left_child, right_child
            self.locked, self.descendants_locked = False, False
            for child_node in (left_child, right_child):
                if child_node:
                    child_node.parent = self

        def is_locked(self):
            return self.locked

        def set_lock(self, lock_state):

            if self.descendants_locked:
                return False  # locked by descendants

            parent_node = self.parent
            while parent_node:  # complexity bounded by tree depth O(h)
                if parent_node.locked:
                    return False  # locked by ancestors
                parent_node = parent_node.parent

            self.locked = lock_state
            parent_node = self.parent  # parent_node
            while parent_node:  # update ancestors inherited locks, complexity bounded by tree depth O(h)
                parent_node.descendants_locked = any(False if node is None else (node.locked or node.descendants_locked)
                                                     for node in (parent_node.left, parent_node.right))
                parent_node = parent_node.parent

            return True

        def lock(self):
            return self.set_lock(True)

        def unlock(self):
            return self.set_lock(False)

    return LockingBinaryTreeNode


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
