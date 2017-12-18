def coding_problem_16():
    """
    You run a sneaker website and want to record the last N order ids in a log. Implement a data structure to
    accomplish this, with the following API:

        record(order_id): adds the order_id to the log
        get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    Example:

    >>> coding_problem_16()
    True
    """
    class OrdersLog(object):

        def __init__(self, num):
            self.circular_buffer = [None] * num
            self.current_index = 0

        def record(self, order_id):
            self.circular_buffer[self.current_index] = order_id
            self.current_index += 1
            if self.current_index == len(self.circular_buffer):
                self.current_index = 0

        def get_last(self, num):
            start_index = self.current_index - num
            if start_index < 0:  # wrap around
                return self.circular_buffer[start_index:] + self.circular_buffer[:self.current_index]
            else:  # no wrapping required
                return self.circular_buffer[start_index:self.current_index]

    log = OrdersLog(10)
    for id in xrange(20):
        log.record(id)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [19])
    assert(log.get_last(5) == range(15, 20))

    log.record(20)
    log.record(21)

    assert(log.get_last(0) == [])
    assert(log.get_last(1) == [21])
    assert(log.get_last(5) == range(17, 22))

    return True


def coding_problem_17(path_str):
    r"""
    Suppose we represent our file system by a string in the following manner:
    The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

        dir
            subdir1
            subdir2
                file.ext

    The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
    The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

        dir
            subdir1
                file1.ext
                subsubdir1
            subdir2
                subsubdir2
                    file2.ext

    The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
    second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a
    file file2.ext.

    We are interested in finding the longest (number of characters) absolute path to a file within our file system.
    For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
    length is 32 (not including the double quotes).

    Given a string representing the file system in the above format, return the length of the longest absolute path to
    a file in the abstracted file system. If there is no file in the system, return 0.

    The name of a file contains at least a period and an extension.
    The name of a directory or sub-directory will not contain a period.
    Example:

    >>> coding_problem_17('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
    32
    """
    if not path_str:
        return 0

    level = 0
    max_len = 0
    dirs = [None]
    tokens = path_str.split('\n')
    for token in tokens:

        tabs = 0
        while token[tabs] == '\t':
            tabs += 1

        if tabs == level:  # substitute current leaf

            dirs[-1] = token

        elif tabs == level + 1:  # go deeper

            level += 1
            dirs.append(token)
            max_len = max(max_len, len(' '.join(map(str.strip, dirs))))

        elif tabs > level + 1:  # malformed string

            raise RuntimeError('Malformed path string')

        else:  # tabs < level

            level = tabs
            dirs = dirs[:level + 1]

    return max_len


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
