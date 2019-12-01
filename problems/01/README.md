## Problem 1

Given a stack of N elements, interleave the first half of the stack
with the second half reversed using one other queue.

Example:

    >>> coding_problem_01([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]
    
    >>> coding_problem_01([1, 2, 3, 4, 5, 6])
    [1, 6, 2, 5, 3, 4]

Note: with the **itertools** module, you could instead:

    islice(chain.from_iterable(izip(l, reversed(l))), len(l))
