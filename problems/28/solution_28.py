def coding_problem_28(word_list, max_line_length):
    """
    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of
    strings which represents each line, fully justified. More specifically, you should have as many words as possible
    in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each
    line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any,
    distributed starting from the left. If you can only fit one word on a line, then you should pad the right-hand side
    with spaces. Each word is guaranteed not to be longer than k.
    Example:

    >>> coding_problem_28(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
    """
    lines = []
    while word_list:

        if len(word_list) == 1:  # right-align ending word
            lines.append('{:>{mll}}'.format(word_list[0], mll=max_line_length))
            break

        words = []
        while len(' '.join(words + word_list[:1])) <= max_line_length and word_list:
            words += word_list[:1]
            word_list = word_list[1:]

        total_spaces = max_line_length - sum(map(len, words))
        gaps = len(words) - 1
        gap_len = total_spaces // gaps
        first_gap_add = total_spaces - gap_len * gaps

        lines.append(words[0] + ' ' * (gap_len + first_gap_add) + (' ' * gap_len).join(words[1:]))

    return lines


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
