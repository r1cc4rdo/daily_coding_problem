## Problem 22

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a
list. If there is more than one possible reconstruction, return any of them. If there is no possible
reconstruction, then return null.

Examples:

    >>> coding_problem_22(['Riccardo', 'Brigittie', 'and', 'lollipop'], 'RiccardoandBrigittie')
    ['Riccardo', 'and', 'Brigittie']

    >>> coding_problem_22(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox')
    ['the', 'quick', 'brown', 'fox']

    >>> coding_problem_22(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond')
    ['bed', 'bath', 'and', 'beyond']
