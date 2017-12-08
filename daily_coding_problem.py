from collections import deque
import numpy as np
import operator
import sys
import os
import re


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


def pn_practice_code_test_a(input_stream=sys.stdin):
    """
    You are given 3 integers a , b , c and a string s. Output result of a+b+c and string s with a half-width break.
    Input will be given in the following format from Standard Input:

    a
    b c
    s

    All integers will be bounded 1 <= a, b, c <= 1000. There will be a half-width break between b and c.
    If we define the length of string s as |s| , it is guaranteed 1 <= |s| <= 100.
    Output the result of a+b+c and string s with a half-width break in one line.
    Make sure to insert a line break at the end of the output.
    Example:

    >>> import cStringIO as StringIO
    >>> pn_practice_code_test_a(StringIO.StringIO(os.linesep.join(['1', '2 3', 'ciao'])))
    '6 ciao'
    """
    a = input_stream.readline()
    b, c = input_stream.readline().split()
    s = input_stream.readline().strip()
    abc = sum(map(int, [a, b, c]))
    return '{} {}'.format(abc, s)


def pn_practice_code_test_b():
    """
    There are N balls labeled with the first N uppercase letters. The balls have pairwise distinct weights.
    You are allowed to ask at most Q queries. In each query, you can compare the weights of two balls.
    Sort the balls in the ascending order of their weights.

    This is an interactive program.
    First, you are given N and Q from Standard Input in the following format:

        N Q

    Then, you start asking queries (at most Q times). Each query must be printed to stdout in the following format:

        ? c1 c2

    Here each of c1 and c2 must be one of the first N uppercase letters, and c1 and c2 must be distinct.
    Then, you are given the answer to the query from Standard Input in the following format:

        ans

    Here ans is either < or >. When ans is <, the ball c2 is heavier than the ball c1, and otherwise the ball c1
    is heavier than the ball c2. Finally, you must print the answer to Standard Output in the following format:

        ! ans

    Here ans must be a string of length N, and it must contain each of the first N uppercase letters once.
    It must represent the weights of the balls in the ascending order.
    """
    def insert(ball, sol):
        """
        Implements a single round of insertion sort with binary search.
        """
        if not sol:
            return [ball]

        half = len(sol) / 2
        pre, mid, post = sol[:half], sol[half], sol[half + 1:]

        print '? {} {}'.format(ball, mid)
        sys.stdout.flush()
        answer = sys.stdin.readline().strip()

        if answer == '<':
            return insert(ball, pre) + [mid] + post
        else:
            return pre + [mid] + insert(ball, post)

    def solve_for_5_7():
        """
        Optimal solution of 5 elements and 7 questions.
        See https://cs.stackexchange.com/questions/44981/least-number-of-comparisons-needed-to-sort-order-5-elements
        """
        print '? A B'
        sys.stdout.flush()
        AB = ['A', 'B'] if sys.stdin.readline().strip() == '<' else ['B', 'A']

        print '? C D'
        sys.stdout.flush()
        CD = ['C', 'D'] if sys.stdin.readline().strip() == '<' else ['D', 'C']

        print '? {} {}'.format(AB[1], CD[1])
        sys.stdout.flush()
        if sys.stdin.readline().strip() == '<':

            triple = AB + [CD[1]]
            leftover = CD[0]

        else:

            triple = CD + [AB[1]]
            leftover = AB[0]

        sol4 = insert('E', triple)
        return insert(leftover, sol4[:3]) + [sol4[-1]]

    alphabet, budget = map(int, sys.stdin.readline().split())
    if alphabet == 5 and budget == 7:

        solution = solve_for_5_7()

    else:

        balls = [chr(0x41 + val) for val in range(alphabet)]
        solution = [balls.pop()]
        while balls:
            solution = insert(balls.pop(), solution)

    print '! {}'.format(''.join(solution))
    sys.stdout.flush()


def lc_basic_calculator(s):
    """
    From https://leetcode.com/problems/basic-calculator
    Examples:

    >>> lc_basic_calculator('1 + 1')
    2
    >>> lc_basic_calculator(' 2-1 + 2 ')
    3
    >>> lc_basic_calculator('(1+(4+5+2)-3)+(6+8)')
    23
    >>> lc_basic_calculator('2-(5-6)')
    3
    """
    class Solution(object):
        def calculate(self, s):
            s = s.replace(' ', '')  # no whitespace
            while '(' in s:  # recursively evaluate sub expressions
                tokens_before = s.split('(')
                token_after = tokens_before[-1].split(')')
                value = self.calculate(token_after[0])
                s = '('.join(tokens_before[:-1]) + str(value) + ')'.join(token_after[1:])
                s = s.replace('--', '+')

            addends = re.split('([+-]?\d+)', s)[1::2]
            return sum(map(int, addends))

    return Solution().calculate(s)


def lc_valid_number(x):
    """
    From https://leetcode.com/problems/valid-number

    Validate if a given string is numeric.
    Note: It is intended for the problem statement to be ambiguous.
    You should gather all requirements up front before implementing one.
    Examples:

    >>> lc_valid_number("0")
    True
    >>> lc_valid_number(" 0.1 ")
    True
    >>> lc_valid_number("abc")
    False
    >>> lc_valid_number("1 a")
    False
    >>> lc_valid_number("2e10")
    True
    """
    class Solution(object):
        @staticmethod
        def is_number(s):
            s = s.strip()
            try:
                _ = float(s)
                return True
            except ValueError:
                return False

    return Solution.is_number(x)


def lc_candies(ratings_list):
    """
    From: https://leetcode.com/problems/candy

    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.

    What is the minimum candies you must give?
    Examples:

    >>> lc_candies([0])
    1
    >>> lc_candies([1, 3, 7, 2, 1, 3, 5, 2, 4])
    17
    """

    class Solution(object):

        @staticmethod
        def compute_gradients(arr):

            padded_arr = np.concatenate((arr[:1], arr, arr[-1:]))
            gradient_left = (padded_arr[1:-1] > padded_arr[:-2]).astype(arr.dtype)
            gradient_right = (padded_arr[1:-1] > padded_arr[2:]).astype(arr.dtype)
            return gradient_left, gradient_right

        def candy(self, ratings_list):

            ratings = np.array(ratings_list)
            candies = np.ones_like(ratings)
            rl, rr = self.compute_gradients(ratings)
            while True:

                cl, cr = self.compute_gradients(candies)
                update = np.maximum(rl - cl, rr - cr)
                if (update == 0).all():
                    break
                candies += update

            return candies.sum()

    return Solution().candy(ratings_list)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
