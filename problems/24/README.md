## Problem 24

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
