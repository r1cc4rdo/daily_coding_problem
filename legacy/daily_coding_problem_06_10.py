def coding_problem_06():
    """
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields, it holds a field named both, which is a XOR of the next node
    and the previous node. Implement a XOR linked list; it has an add(element) which adds the element to the end,
    and a get(index) which returns the node at index.
    Example:

    >>> l = coding_problem_06()
    >>> for cnt in range(0, 4):
    ...     l.add(cnt)
    >>> l.get(2) == 2
    True

    Note: python does not have actual pointers (id() exists but it is not an actual pointer in all implementations).
    For this reason, we use a python list to simulate memory. Indexes are the addresses in memory. This has the
    unfortunate consequence that the travel logic needs to reside in the List class rather than the Node one.
    """
    class XORLinkedListNode(object):

        def __init__(self, val, prev, next):
            self.val = val
            self.both = prev ^ next

        def next_node(self, prev_idx):
            return self.both ^ prev_idx

        def prev_node(self, next_idx):
            return self.both ^ next_idx

    class XORLinkedList(object):

        def __init__(self):
            self.memory = [XORLinkedListNode(None, -1, -1)]

        def head(self):
            return 0, -1, self.memory[0]  # head node index, prev node index, head node

        def add(self, val):
            current_node_index, previous_node_index, current_node = self.head()
            while True:  # walk down the list until we find the end
                next_node_index = current_node.next_node(previous_node_index)
                if next_node_index == -1:  # we reached the end on the list
                    break
                previous_node_index, current_node_index = current_node_index, next_node_index
                current_node = self.memory[next_node_index]

            new_node_index = len(self.memory)  # "allocation"
            current_node.both = previous_node_index ^ new_node_index
            self.memory.append(XORLinkedListNode(val, current_node_index, -1))

        def get(self, index):
            current_index, previous_index, current_node = self.head()
            for cnt in range(index + 1):
                previous_index, current_index = current_index, current_node.next_node(previous_index)
                current_node = self.memory[current_index]
            return current_node.val

    return XORLinkedList()


def coding_problem_07(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    Examples:

    >>> coding_problem_07('111')  # possible interpretations: 'aaa', 'ka', 'ak'
    3
    >>> coding_problem_07('2626')  # 'zz', 'zbf', 'bfz', 'bfbf'
    4
    """
    symbols = map(str, range(1, 27))
    if not s:
        return 1

    matches = filter(lambda symbol: s.startswith(symbol), symbols)
    encodings = [coding_problem_07(s[len(m):]) for m in matches]
    return sum(encodings)


def coding_problem_08(btree):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes have the same value.
    Given the root to a binary tree, count the number of unival subtrees.
    Example:

    >>> btree = (0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))
    >>> coding_problem_08(btree)[0]
    6
    """
    val, ln, rn = btree
    if ln is None and rn is None:  # leaf case
        return 1, True, val

    lcount, is_uni_l, lval = coding_problem_08(ln)
    rcount, is_uni_r, rval = coding_problem_08(rn)

    is_unival = is_uni_l and is_uni_r and val == lval and val == rval
    count = lcount + rcount + is_unival
    return count, is_unival, val


def coding_problem_09(numbers):
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
    The "largest sum of non-adjacent numbers" is the sum of any subset of non-contiguous elements.
    Solution courtesy of Kye Jiang (https://github.com/Jedshady).
    Examples:

    >>> coding_problem_09([2, 4, 6, 8])
    12
    >>> coding_problem_09([5, 1, 1, 5])
    10
    >>> coding_problem_09([1, 2, 3, 4, 5, 6])
    12
    >>> coding_problem_09([-8, 4, -3, 2, 3, 4])
    10
    >>> coding_problem_09([2, 4, 6, 2, 5])
    13
    """
    if not numbers:
        return 0

    if len(numbers) <= 2:
        return max(numbers)

    with_last = coding_problem_09(numbers[:-2]) + numbers[-1]  # sum include last number
    without_last = coding_problem_09(numbers[:-1])  # sum without last number
    return max(with_last, without_last)


def coding_problem_10():
    """
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    Example:

    >>> coding_problem_10()
    Before
    Hello from thread
    After
    """
    from threading import Thread
    import time

    def delayed_execution(f, ms):
        time.sleep(ms)
        return f()

    def hello(name):
        print('Hello {}'.format(name))

    job = Thread(target=delayed_execution, args=(lambda: hello('from thread'), 0.01))
    job.start()

    print('Before')
    time.sleep(0.02)
    print('After')


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
