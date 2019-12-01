##Problem 34

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
lexicographically earliest one (the first one alphabetically).
Examples:

    >>> coding_problem_34("race")
    'ecarace'
    >>> coding_problem_34("google")
    'elgoogle'
    >>> coding_problem_34("aibohphobia")
    'aibohphobia'

Note: this is similar to #31.
For each given word w, there are 2*len(w)-1 possible palindromes made using as centers either a character (len(w))
or the location between two characters (len(w)-1).