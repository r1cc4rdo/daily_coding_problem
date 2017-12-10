import sys
import os


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


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
