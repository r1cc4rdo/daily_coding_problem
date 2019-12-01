def coding_problem_29(rle):
    """
    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
    successive characters as a single count and character. Implement run-length encoding and decoding. You can assume
    the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to
    be decoded is valid.
    Examples:

    >>> coding_problem_29('AAAABBBCCDAA')
    '4A3B2C1D2A'
    >>> coding_problem_29('4A3B2C1D2A')
    'AAAABBBCCDAA'
    """
    if rle.isalpha():  # no numbers, encode

        encoded = ''
        while rle:

            idx = 0
            while idx < len(rle) and rle[0] == rle[idx]:
                idx += 1

            encoded += str(idx) + rle[0]
            rle = rle[idx:]

        return encoded

    else:  # decode

        return ''.join(c * int(n) for n, c in zip(rle[::2], rle[1::2]))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
