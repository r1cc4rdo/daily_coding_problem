def coding_problem_22(dictionary, the_string):
    """
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
    """
    result = []
    while the_string:

        found = False
        for word in dictionary:

            if the_string.startswith(word):

                the_string = the_string[len(word):]
                result += [word]
                found = True
                break

        if not found:
            return None

    return result


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
