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


def pn_edit_distance(input_stream=sys.stdin):
    """
    Verify if the edit distance between two strings is lower or equal to one.
    Edit distance considers character insertion, deletion and substitution as basic operations.
    Output 'YES' is the two provided strings have an edit distance lower than 1, 'NO' otherwise.
    Examples:

    >>> import cStringIO as StringIO
    >>> pn_edit_distance(StringIO.StringIO(os.linesep.join(['abcde', 'abcfe'])))
    YES
    >>> pn_edit_distance(StringIO.StringIO(os.linesep.join(['abcde', 'abde'])))
    YES
    >>> pn_edit_distance(StringIO.StringIO(os.linesep.join(['abcdef', 'abcde'])))
    YES
    >>> pn_edit_distance(StringIO.StringIO(os.linesep.join(['abcde', 'abdce'])))
    NO
    """
    S = input_stream.readline().strip()
    T = input_stream.readline().strip()

    if len(S) < len(T):
        S, T = T, S

    if S == T:

        print 'YES'

    elif len(S) - len(T) > 1:

        print 'NO'

    else:

        while T:  # remove equal prefix

            if S[0] == T[0]:

                S = S[1:]
                T = T[1:]

            else:

                break

        print 'YES' if len(T) <= 1 or S[1:] == T or S[1:] == T[1:] else 'NO'


def pn_strings_wo_repetitions(input_stream=sys.stdin):
    """
    Given a list of characters, return the number of string than can be composed from all of them without any two
    adjacent characters being equal.

    >>> import cStringIO as StringIO
    >>> pn_strings_wo_repetitions(StringIO.StringIO('aabb' + os.linesep))
    2
    >>> pn_strings_wo_repetitions(StringIO.StringIO('aabbbccd' + os.linesep))
    384
    """

    S = input_stream.readline().strip()

    def add(prefix, characters):

        if not characters:
            return 1  # leaf case

        last_char = prefix[-1] if prefix else None
        valid_characters = [c for c in characters if c != last_char]
        if not valid_characters:
            return 0  # infeasible

        count = 0
        for c in set(valid_characters):
            rest_of_string = list(characters)  # copy
            rest_of_string.remove(c)
            count += add(prefix + c, rest_of_string)

        return count

    return  add('', list(S))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
