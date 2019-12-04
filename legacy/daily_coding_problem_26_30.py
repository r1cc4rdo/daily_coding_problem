try:
    from future.utils import implements_iterator
except ImportError:
    pass

try:
    from functools import reduce
except ImportError:
    pass


def coding_problem_26(not_a_linked_list, k):
    """
    Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
    smaller than the length of the list. The list is very long, so making more than one pass is prohibitively expensive.
    Do this in constant space and in one pass.

    >>> coding_problem_26(range(10), 3)
    [0, 1, 2, 3, 4, 5, 6, 7, 9]

    Note: not using a linked list out of convenience, but moving through it with iterators which do have a similar
    usage patterns.

    Note2: what I coded below was my first and only solution. However, using two pointers/indexes/iterators equates to
    two passes in my book. I checked on Google, and all the solutions are equivalent to this. The alternative, a
    k-buffer of the stream, would not be constant space. If you're reading this and have better ideas, let me know!
    """
    iter_to_the_end = iter(not_a_linked_list)
    for _ in range(k):
        next(iter_to_the_end)  # k is guaranteed < len(list)

    result = []
    iter_lagging_behind = iter(not_a_linked_list)
    while True:
        result.append(next(iter_lagging_behind))
        try:
            next(iter_to_the_end)
        except StopIteration:
            break

    next(iter_lagging_behind)  # gobble an element
    result.extend(iter_lagging_behind)
    return result


def coding_problem_27(brace_yourself):
    """
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are
    balanced (well-formed).
    Examples:

    >>> coding_problem_27('([])[]({})')
    True
    >>> coding_problem_27('([)]')
    False
    >>> coding_problem_27('((()')
    False

    Note: I get it. This wants me to keep track of all opening parenthesis in a stack, and remove the top after
    encountering a closing one, provided it's of the matching type. Easy enough, BUT! such an algorithm requires lots of
    bookkeeping and it's inherently sequential. My implementation below works in a number of passes that only depends
    on the nesting levels of the braces; memory usage is O(n) for both solutions. Also, string operations are highly
    optimized, making this even faster.
    """
    copy = None
    while brace_yourself and brace_yourself != copy:

        copy = brace_yourself
        brace_yourself = reduce(lambda s, p: s.replace(p, ''), ['()', '[]', '{}'], brace_yourself)

    return brace_yourself == ''


def coding_problem_28(word_list, max_line_length):
    """
    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of
    strings which represents each line, fully justified. More specifically, you should have as many words as possible
    in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each
    line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any,
    distributed starting from the left. If you can only fit one word on a line, then you should pad the right-hand side
    with spaces. Each word is guaranteed not to be longer than k.
    Example:

    >>> coding_problem_28(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
    """
    lines = []
    while word_list:

        if len(word_list) == 1:  # right-align ending word
            lines.append('{:>{mll}}'.format(word_list[0], mll=max_line_length))
            break

        words = []
        while len(' '.join(words + word_list[:1])) <= max_line_length and word_list:
            words += word_list[:1]
            word_list = word_list[1:]

        total_spaces = max_line_length - sum(map(len, words))
        gaps = len(words) - 1
        gap_len = total_spaces // gaps
        first_gap_add = total_spaces - gap_len * gaps

        lines.append(words[0] + ' ' * (gap_len + first_gap_add) + (' ' * gap_len).join(words[1:]))

    return lines

def coding_problem_29(rle):
    """
    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
    successive characters as a single count and character. Implement run-length encoding and decoding. You can assume
    the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to
    be decoded is valid.
    Examples:

    >>> coding_problem_29('AAAABBBCCDAA')
    '4A3B2C1D2A'
    >>> coding_problem_29('4A3B2C1D2A')
    'AAAABBBCCDAA'
    """
    if rle.isalpha():  # no numbers, encode

        encoded = ''
        while rle:

            idx = 0
            while idx < len(rle) and rle[0] == rle[idx]:
                idx += 1

            encoded += str(idx) + rle[0]
            rle = rle[idx:]

        return encoded

    else:  # decode

        return ''.join(c * int(n) for n, c in zip(rle[::2], rle[1::2]))


def coding_problem_30(arr):
    """
    You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
    is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled
    up. Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
    Examples:

    >>> coding_problem_30([2, 1, 2])  # 1@1, 1 unit of water at index 1
    1
    >>> coding_problem_30([3, 0, 1, 3, 0, 5])  # 3@1 2@2 3@4
    8
    >>> coding_problem_30([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 1@2 1@4 2@5 1@6 1@9
    6
    """
    water = 0
    while len(arr) > 2:

        lval = arr[0]  # the idea is: from the smallest left/right boundary, accumulate water level until reaching a
        rval = arr[-1]  # higher wall inside. Then recurse with with the new bound, until only two array entries.
        if lval <= rval:

            cnt = 1
            while arr[cnt] < arr[0]:
                water += arr[0] - arr[cnt]
                cnt += 1

            arr = arr[cnt:]

        else:

            cnt = -2
            while arr[cnt] < arr[-1]:
                water += arr[-1] - arr[cnt]
                cnt -= 1

            arr = arr[:cnt+1]

    return water


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
