## [<<](../24) [25] Implement regular expression matcher [>>](../26)

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
