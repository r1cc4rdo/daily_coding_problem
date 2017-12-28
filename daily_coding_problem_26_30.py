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
    for _ in xrange(k):
        iter_to_the_end.next()  # k is guaranteed < len(list)

    result = []
    iter_lagging_behind = iter(not_a_linked_list)
    while True:
        result.append(iter_lagging_behind.next())
        try:
            iter_to_the_end.next()
        except StopIteration:
            break

    iter_lagging_behind.next()  # gobble an element
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


def coding_problem_28():
    """

    >>> coding_problem_28()

    """
    pass


def coding_problem_29():
    """

    >>> coding_problem_29()

    """
    pass


def coding_problem_30():
    """

    >>> coding_problem_30()

    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
