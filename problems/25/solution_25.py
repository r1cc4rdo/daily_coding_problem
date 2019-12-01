def coding_problem_25(rexp, string):
    """
    Implement regular expression matching with the following special characters:

        . (period) which matches any single character
        * (asterisk) which matches zero or more of the preceding element

    That is, implement a function that takes in a string and a valid regular expression and returns whether or not the
    string matches the regular expression.
    Examples:

    >>> coding_problem_25('ra.', 'ray')
    True
    >>> coding_problem_25('ra.', 'raymond')
    False
    >>> coding_problem_25('.*at', 'chat')
    True
    >>> coding_problem_25('.*at', 'chats')
    False
    """
    while rexp and string:

        if len(rexp) >= 2 and rexp[1] == '*':

            for cnt in xrange(len(string)):
                if coding_problem_25(''.join([rexp[0]] * cnt) + rexp[2:], string):
                    return True

            return False

        else:

            if rexp[0] != '.' and rexp[0] != string[0]:
                return False

            rexp = rexp[1:]
            string = string[1:]

    return all([not rexp, not string])


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)