def coding_problem_16():
    """
    You run a sneaker website and want to record the last N order ids in a log. Implement a data structure to
    accomplish this, with the following API:

        record(order_id): adds the order_id to the log
        get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    Example:

    >>> coding_problem_16()
    True
    """
    class OrdersLog(object):

        def __init__(self, num):
            self.circular_buffer = [None] * num
            self.current_index = 0

        def record(self, order_id):
            self.circular_buffer[self.current_index] = order_id
            self.current_index += 1
            if self.current_index == len(self.circular_buffer):
                self.current_index = 0

        def get_last(self, num):
            start_index = self.current_index - num
            if start_index < 0:  # wrap around
                return self.circular_buffer[start_index:] + self.circular_buffer[:self.current_index]
            else:  # no wrapping required
                return self.circular_buffer[start_index:self.current_index]

    log = OrdersLog(10)
    for id in xrange(20):
        log.record(id)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [19])
    assert(log.get_last(5) == range(15, 20))

    log.record(20)
    log.record(21)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [21])
    assert(log.get_last(5) == range(17, 22))

    return True


def coding_problem_17(path_str):
    """
    Suppose we represent our file system by a string in the following manner:
    The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

        dir
            subdir1
            subdir2
                file.ext

    The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
    The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

        dir
            subdir1
                file1.ext
                subsubdir1
            subdir2
                subsubdir2
                    file2.ext

    The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
    second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a
    file file2.ext.

    We are interested in finding the longest (number of characters) absolute path to a file within our file system.
    For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
    length is 32 (not including the double quotes).

    Given a string representing the file system in the above format, return the length of the longest absolute path to
    a file in the abstracted file system. If there is no file in the system, return 0.

    The name of a file contains at least a period and an extension.
    The name of a directory or sub-directory will not contain a period.
    Example:

    >>> coding_problem_17('dir\n\tfile1.ext')
    13
    >>> coding_problem_17('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
    32
    >>> coding_problem_17('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\ndir2\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\t\t\tsubsubsubdir3\n\t\t\t\tfile3.ext')
    47
    """
    class Node(object):
        '''
        Node of a Directory N-ary Tree
        '''
        def __init__(self, val=None, level=None, parent=None, is_file=False):
            self.val = val
            self.level = level
            self.parent = parent
            self.subdir = list()    # Node's children as a list
            self.is_file =is_file

        def add_node(self, node=None):
            self.subdir.append(node)

        def get_parent(self):
            return self.parent


    class Tree(object):
        '''
        A Directory N-ary Tree
        '''
        def __init__(self, root=None):
            self.root = Node('*', -1)


    def build_tree(path_str):
        '''
        Build a directory n-ary tree
        Args:
            path_str(string): a string represented a fild system path
        Returns:
            Tree: a directory tree
        '''
        path_dir = path_str.split('\n')
        dir_tree = Tree()
        cur_level = -1
        cur_root = dir_tree.root

        for token in path_dir:
            tabs = 0
            while token[tabs] == '\t':
                tabs += 1

            if cur_level >= tabs:   # need to back track the parent node
                i = cur_level - tabs + 1
                while i != 0:
                    cur_root = cur_root.get_parent()
                    i -= 1

            if len(token.split('.')) > 1:   # is a file
                new_node = Node(token[tabs:], tabs, cur_root, True)
            else:   # not a file
                new_node = Node(token[tabs:], tabs, cur_root)

            cur_root.add_node(new_node)
            cur_level = tabs
            cur_root = new_node

        return dir_tree


    def lgst_file_path(node):
        '''
        Given a tree node, find the longest absolute path to a file
        Args:
            node(Node): a tree node
        Returns:
            int: the length of the longest path
        '''
        if node.is_file:    # hit a leaf, and leaf is a file
            return len(node.val)
        if len(node.subdir) == 0:   # hit a leaf but a dir
            return 0

        max_len = 0
        for sub_node in node.subdir:
            max_len = max(max_len, lgst_file_path(sub_node))

        # node.level < 0 means this node is root
        length = max_len if node.level < 0 else max_len + len(node.val) + 1

        return length

    tree = build_tree(path_str)
    return lgst_file_path(tree.root)


def coding_problem_18(arr, k):
    """
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
    sub-array of length k. Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not
    need to store the results. You can simply print them out as you compute them.
    Example:

    >>> coding_problem_18([10, 5, 2, 7, 8, 7], 3)
    [10, 7, 8, 8]
    """
    for cnt in xrange(k - 1):
        arr = [max(index, next) for index, next in zip(arr[:-1], arr[1:])]

    return arr


def coding_problem_19(costs):
    """
    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
    while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and
    kth column represents the cost to build the nth house with kth color, return the minimum cost.
    """
    best_cost = [0] * len(costs[0])
    for cost in costs:  # add a house at a time
        for index in xrange(len(cost)):  # best cost is the one for that color plus min cost between every other color
            best_cost[index] = cost[index] + min(best_cost[:index] + best_cost[index + 1:])

    return min(best_cost)


def coding_problem_20():
    """
    Given two singly linked lists that intersect at some point, find the intersecting node.
    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
    For example, given A = 3 -> 7 -> 8 -> 10 -> 1 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

    >>> coding_problem_20()
    8

    Note: the problem statement above is ambiguous and misleading. I think B list was originally supposed to end
    up with a -> 1. This is how most problems of this type I googled are formulated. If this is not the case, this
    is akin to finding the longest common list between the lists, which I believe cannot be solved in O(M+N).
    """
    class LinkedListNode(object):

        def __init__(self, value, child=None):
            self.value = value
            self.next = child

        def add(self, value):
            return LinkedListNode(value, self)

        @classmethod
        def len(cls, node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count

    common_tail = LinkedListNode(1).add(10).add(8)
    list_a = LinkedListNode(7, common_tail).add(3)
    list_b = LinkedListNode(1, common_tail).add(99).add(14)

    len_a = LinkedListNode.len(list_a)
    len_b = LinkedListNode.len(list_b)
    if len_b > len_a:
        list_a, list_b = list_b, list_a

    for advance in xrange(abs(len_a - len_b)):
        list_a = list_a.next

    for check in xrange(len_b):
        if list_a is list_b:
            return list_a.value

        list_a = list_a.next
        list_b = list_b.next

    return None


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
