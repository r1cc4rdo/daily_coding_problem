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
    class LockingBinaryTreeNode(object):

        def __init__(self, p, l=None, r=None):
            self.left = l
            self.right = r
            self.parent = p
            self.lock = False

        def is_locked(self):
            return self.lock

        def can_lock(self):
            walk_up = self
            while walk_up:
                if walk_up.lock:
                    return False
                walk_up = walk_up.parent
            return self.recursive_walk_down(self.left) and self.recursive_walk_down(self.right)

        @staticmethod
        def recursive_walk_down(node):

            if node is None:
                return True

            if node.lock:
                return False

            return LockingBinaryTreeNode.recursive_walk_down(node.left) and \
                   LockingBinaryTreeNode.recursive_walk_down(node.right)

        def set_lock_state(self, lock_state):
            success = self.can_lock()
            if success:
                self.lock = lock_state
            return success

        def lock(self):
            return self.set_lock_state(True)

        def unlock(self):
            return self.set_lock_state(False)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
