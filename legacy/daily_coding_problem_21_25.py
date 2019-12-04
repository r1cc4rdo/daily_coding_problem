def coding_problem_21(times):
    """
    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
    find the minimum number of rooms required.
    Example:

    >>> coding_problem_21([(30, 75), (0, 50), (60, 150)])
    2
    """
    start_times = [(t[0], 1) for t in times]  # [(30, 1), (0, 1), (60, 1)]
    end_times = [(t[1], -1) for t in times]  # [(75, -1), (50, -1), (150, -1)]
    room_allocation = [t[1] for t in sorted(start_times + end_times, key=lambda t: t[0])]  # [1, 1, -1, 1, -1, -1]

    rooms, max_rooms = 0, 0
    for event in room_allocation:
        rooms += event  # occupied or released
        max_rooms = max(max_rooms, rooms)
    assert(rooms == 0)

    return max_rooms


def coding_problem_22(dictionary, the_string):
    """
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a
    list. If there is more than one possible reconstruction, return any of them. If there is no possible
    reconstruction, then return null.
    Examples:

    >>> coding_problem_22(['Riccardo', 'Brigittie', 'and', 'lollipop'], 'RiccardoandBrigittie')
    ['Riccardo', 'and', 'Brigittie']

    >>> coding_problem_22(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox')
    ['the', 'quick', 'brown', 'fox']

    >>> coding_problem_22(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond')
    ['bed', 'bath', 'and', 'beyond']
    """
    result = []
    while the_string:

        found = False
        for word in dictionary:

            if the_string.startswith(word):

                the_string = the_string[len(word):]
                result += [word]
                found = True
                break

        if not found:
            return None

    return result


def coding_problem_23(matrix, start, end):
    """
    You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
    Each False boolean represents a tile you can walk on. Given this matrix, a start coordinate, and an end coordinate,
    return the minimum number of steps required to reach the end coordinate from the start. If there is no possible
    path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap
    around the edges of the board.
    Examples:

    >>> map = [[False, False, False, False], [True, True, False, True],
    ...        [False, False, False, False], [False, False, False, False]]
    >>> coding_problem_23(map, (3, 0), (0, 0))
    7
    >>> map[1][2] = True  # close off path
    >>> coding_problem_23(map, (3, 0), (0, 0))  # None
    """
    coords = [(index_r, index_c) for index_r, row in enumerate(matrix)
              for index_c, element in enumerate(row) if not element]

    current_distance = 0
    distances = [[None for col in range(len(matrix[0]))] for row in range(len(matrix))]
    distances[start[0]][start[1]] = 0
    while True:

        wavefront = [coord for coord in coords if distances[coord[0]][coord[1]] == current_distance]
        if not wavefront:
            break

        current_distance += 1
        for node in wavefront:

            neighbours = [coord for coord in coords if (abs(node[0] - coord[0]) + abs(node[1] - coord[1])) == 1]
            for n in neighbours:
                if distances[n[0]][n[1]] is None:
                    distances[n[0]][n[1]] = current_distance

    return distances[end[0]][end[1]]


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


def coding_problem_25(rexp, string):
    """
    Implement regular expression matching with the following special characters:

        . (period) which matches any single character
        * (asterisk) which matches zero or more of the preceding element

    That is, implement a function that takes in a string and a valid regular expression and returns whether or not the
    string matches the regular expression.
    Examples:

    >>> coding_problem_25('ra.', 'ray')
    True
    >>> coding_problem_25('ra.', 'raymond')
    False
    >>> coding_problem_25('.*at', 'chat')
    True
    >>> coding_problem_25('.*at', 'chats')
    False
    """
    while rexp and string:

        if len(rexp) >= 2 and rexp[1] == '*':

            for cnt in range(len(string)):
                if coding_problem_25(''.join([rexp[0]] * cnt) + rexp[2:], string):
                    return True

            return False

        else:

            if rexp[0] != '.' and rexp[0] != string[0]:
                return False

            rexp = rexp[1:]
            string = string[1:]

    return all([not rexp, not string])


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
