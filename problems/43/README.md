## [<<](../42) Problem 43 [>>](../44)

Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

Example:

    >>> max_stack = coding_problem_43()
    >>> max_stack.push(1)
    >>> max_stack.max()
    1

    >>> max_stack.push(3)
    >>> max_stack.max()
    3

    >>> max_stack.push(2)
    >>> max_stack.max()
    3

    >>> max_stack.pop()
    2

    >>> max_stack.max()
    3

    >>> _ = max_stack.pop()
    >>> max_stack.max()
    1

    >>> _ = max_stack.pop()
    >>> max_stack.max()
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    
    >>> _ = max_stack.pop()
    Traceback (most recent call last):
    ...
    IndexError: pop from empty list
