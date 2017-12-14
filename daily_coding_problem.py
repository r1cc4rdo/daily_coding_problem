from collections import deque
import numpy as np


def coding_problem_1(stack):
    """
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using one other queue.
    Example:

    >>> coding_problem_1([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]
    >>> coding_problem_1([1, 2, 3, 4, 5, 6])
    [1, 6, 2, 5, 3, 4]

    Note: with Python lists, you could instead islice(chain.from_iterable(izip(l, reversed(l))), len(l))
    """
    queue = deque([])  # stack S:[1,2,3,4,5], queue Q:[]
    for cnt in xrange(len(stack) - 1):  # move stack into queue. S:[1], Q:[5,4,3,2]
        queue.append(stack.pop())
    for cnt in xrange(len(queue) / 2):
        stack.append(queue.popleft())  # S:[1,5], Q:[4,3,2]
        for cnt2 in xrange(len(queue) - 1):  # rotate last element to front, S:[1,5], Q:[2,4,3]
            queue.append(queue.popleft())
        stack.append(queue.popleft())  # S:[1,5,2], Q:[4,3]
    if queue:
        stack.append(queue.popleft())
    return stack


def coding_problem_2(l):
    """
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one at i.
    Solve it without using division and in O(n).
    Example:

    >>> coding_problem_2([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    """
    result = np.ones(len(l), dtype=type(l[0]))
    for idx in xrange(len(l)):
        prev = result[idx]
        result *= l[idx]
        result[idx] = prev
    return list(result)


def coding_problem_3():
    """
    Given the root to a binary tree, implement serialize(root), which serializes the tree
    into a string, and deserialize(s), which deserializes the string back into the tree.
    Example:

    >>> coding_problem_3()
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
            val, lc, rc = queue.popleft(), None, None
            if val is not None:
                lc = cls.deserialize(queue)
                rc = cls.deserialize(queue)
            return BinaryNode(val, lc, rc)

    serialized_tree = [3, 2, 1, None, None, None, 4, 5, None, None, 6, None, None]
    de_serialized = BinaryNode.deserialize(deque(serialized_tree))
    re_serialized = de_serialized.serialize()
    return serialized_tree == re_serialized


def coding_problem_4(arr):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    You can modify the input array in-place.
    Example:

    >>> coding_problem_4([3, 4, -1, 1])
    2
    >>> coding_problem_4([1, 2, 0])
    3
    >>> coding_problem_4([4, 1, 2, 2, 2, 1, 0])
    3
    """
    arr = np.array(arr)
    arr = arr[arr > 0]
    while True:
        prev_arr, arr = arr, arr[arr <= len(arr)]
        if np.array_equal(arr, prev_arr):
            break

    arr[arr - 1] = arr  # magic in-place bucket sort
    idxs = np.argwhere(arr != range(1, 1 + len(arr))).flatten()
    return 1 + (arr[-1] if len(idxs) == 0 else idxs[0])


def coding_problem_5():
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    Given this implementation of cons below, implement car and cdr.
    Examples: car(cons(3, 4)) == 3, cdr(cons(3, 4)) == 4

    >>> coding_problem_5()
    True
    """
    def cons(a, b):
        return lambda f: f(a, b)

    def car(f):
        return f(lambda a, b: a)

    def cdr(f):
        return f(lambda a, b: b)

    return car(cons(3, 4)) == 3 and cdr(cons(3, 4)) == 4


def coding_problem_6():
    """
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields, it holds a field named both, which is a XOR of the next node
    and the previous node. Implement a XOR linked list; it has an add(element) which adds the element to the end,
    and a get(index) which returns the node at index.
    Example:

    >>> coding_problem_6()
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
            for cnt in xrange(index + 1):
                previous_index, current_index = current_index, current_node.next_node(previous_index)
                current_node = self.memory[current_index]
            return current_node.val

    l = XORLinkedList()
    for cnt in xrange(0, 4):
        l.add(cnt)

    return l.get(2) == 2


def coding_problem_7(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    Example:

    The message '111' gives 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    >>> coding_problem_7('111')
    3

    The message '2626' gives 4, since it could be decoded as 'zz', 'zbf', 'bfz' and 'bfbf'.
    >>> coding_problem_7('2626')
    4
    """
    symbols = map(str, range(1, 27))
    if not s:
        return 1

    matches = filter(lambda symbol: s.startswith(symbol), symbols)
    encodings = [coding_problem_7(s[len(m):]) for m in matches]
    return sum(encodings)


def coding_problem_8(btree):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes have the same value.
    Given the root to a binary tree, count the number of unival subtrees.
    Example:

    >>> btree = (0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))
    >>> coding_problem_8(btree)[0]
    6
    """
    val, ln, rn = btree
    if ln is None and rn is None:  # leaf case
        return 1, True, val

    lcount, is_uni_l, lval = coding_problem_8(ln)
    rcount, is_uni_r, rval = coding_problem_8(rn)

    is_unival = is_uni_l and is_uni_r and val == lval and val == rval
    count = lcount + rcount + is_unival
    return count, is_unival, val


def coding_problem_9(arr):
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
    Examples:

    >>> coding_problem_9([2, 4, 6, 8])
    12
    >>> coding_problem_9([5, 1, 1, 5])
    10
    """
    assert(len(arr) >= 3)

    max_sum = 0
    for cnt in xrange(0, len(arr)):

        sum = arr[cnt] + max(arr[:cnt-1] + arr[cnt+2:])
        max_sum = max(max_sum, sum)

    return max_sum


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
        print 'Hello {}'.format(name)

    job = Thread(target=delayed_execution, args=(lambda: hello('from thread'), 0.01))
    job.start()

    print 'Before'
    time.sleep(0.02)
    print 'After'


def coding_problem_11(strings, prefix):
    """
    Implement an autocomplete system. That is, given a query string s and a dictionary of all possible query strings,
    return all strings in the dictionary that have s as a prefix. Hint: Try pre-processing the dictionary into a more
    efficient data structure to speed up queries.
    Example:

    >>> words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
    >>> coding_problem_11(words, 'abo')
    ['abode', 'about', 'above']

    Note: I have been thinking of lots of potential data structures, like hierarchical dictionaries, or hashing.
    Unless otherwise specified, I think space/computation trade-off is not worth doing more than I do below.
    The necessity of using more sophisticated solutions depends on the problem to be solved, overkill here.
    """
    def binary_search(list_like, item, mode='any', fmap=None):
        """
        Pretty pleased with this binary search function. Supports searching for the first, last or any match with
        the given item. Both the elements of the list and the item can be optionally mapped through a function which
        should output items that support the standard ordering operators.
        """
        fmap = fmap if fmap else lambda x: x
        fitem = fmap(item)

        first = 0
        last = len(list_like) - 1
        while first < last:

            midpoint = (first + last) // 2
            if fmap(list_like[midpoint]) == fitem:

                if mode == 'first':  # continue searching for the first occurrence of item

                    last = midpoint

                elif mode == 'last':  # continue searching for the last occurrence of item

                    if midpoint == first:  # end game

                        if fmap(list_like[last]) == fitem:

                            first += 1

                        else:

                            last -= 1

                    else:  # more than 1 item apart

                        first = midpoint

                else:  # return the index of any occurrence of item

                    return midpoint

            elif fitem < fmap(list_like[midpoint]):

                last = midpoint - 1

            else:

                first = midpoint + 1

        return first if fmap(list_like[first]) == fitem else -1

    strings = [s.lower() for s in sorted(strings)]
    s = binary_search(strings, prefix, 'first', fmap=lambda s: s[:min(3, len(s))])
    e = binary_search(strings, prefix, 'last', fmap=lambda s: s[:min(3, len(s))])
    return strings[s:(e+1)]


def coding_problem_12(budget, choices):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a
    function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
    integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    Example:

    >>> coding_problem_12(4, [1, 2])
    5
    """
    if budget == 0:
        return 1  # leaf case

    available_choices = [c for c in choices if c <= budget]
    if not available_choices:
        return 0  # unfeasible

    count = 0
    for c in available_choices:
        count += coding_problem_12(budget - c, choices)

    return count


def coding_problem_13(s, k):
    """
    Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
    characters.
    Example:

    >>> coding_problem_13('abcba', 2)  # longest substring with at most 2 distinct characters is 'bcb'
    3
    >>> coding_problem_13('edabccccdccba', 3)  # 'bccccdccb'
    9
    """
    assert(len(s) >= k)

    start_index, end_index, max_length = 0, k, k
    while end_index < len(s):

        end_index += 1
        while True:

            distinct_characters = len(set(s[start_index:end_index]))
            if distinct_characters <= k:
                break

            start_index += 1

        max_length = max(max_length, end_index - start_index)

    return max_length


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
