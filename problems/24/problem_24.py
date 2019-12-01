def coding_problem_24():
    """
    Implement locking in a binary tree. A binary tree node can be locked or unlocked only if any of its descendants or
    ancestors are not locked. Write a binary tree node class with the following methods:

        is_locked, which returns whether the node is locked
        lock, which attempts to lock the node. If it cannot be locked, then it should return false.
            Otherwise, it should lock it and return true.
        unlock, which unlocks the node

    You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
    Each method should run in O(h), where h is the height of the tree.

    Note: [TODO] missing unit test for # 24
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
