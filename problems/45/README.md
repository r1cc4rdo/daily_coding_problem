## [<<](../44) [45] Implement rand [>>](../46)

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
function rand7() that returns an integer from 1 to 7 (inclusive).

Example:

    >>> from random import randint
    >>> rand5 = lambda: randint(0, 4)
    >>> rand7 = coding_problem_45(rand5)
    >>> 0 <= rand7 < 7
    True
