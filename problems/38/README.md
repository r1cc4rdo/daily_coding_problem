## [<<](../37) [38] Solve the N-queens problem [>>](../39)

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
column, or diagonal.

The following are the first 7 terms of the sequence (from [Wikipedia's Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) page):

    >>> [coding_problem_38(n + 1) for n in range(7)]
    [1, 0, 0, 2, 10, 4, 40]
