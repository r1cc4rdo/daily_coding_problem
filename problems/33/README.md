##Problem 33

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
the list so far on each new element. Recall that the median of an even-numbered list is the average of the two
middle numbers. Example:

    >>> coding_problem_33([2, 1, 5, 7, 2, 0, 5])
    [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]

Note: cheating with numpy below, but I see no reason to make it more complicated given the request. An efficient
implementation would keep sorted in place the first n elements and do an insertion sort pass each time.