## [<<](../16) [17] Longest path in a filesystem [>>](../18)

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

Examples:

    >>> coding_problem_17('file1.ext')
    9

    >>> coding_problem_17('dir\n\tfile1.ext')
    13

    >>> coding_problem_17('0\n\t23.567\n12345.789')
    9

    >>> coding_problem_17('dir\n\t\tfile1.ext')
    Traceback (most recent call last):
    ...
    RuntimeError: Malformed path string: nesting more than one level at a time.

    >>> coding_problem_17('dir\n\tfile1.ext\n\t\tchild_of_a_file.ext')
    Traceback (most recent call last):
    ...
    RuntimeError: Malformed path string: a file cannot contain something else.

    >>> coding_problem_17('dir\n\tfile1.ext\n\tsubdir\n\t\tsubsubdir\n\t\t\ttsubsubsubdir')
    13

    >>> coding_problem_17('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
    32

    >>> coding_problem_17('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' +
    ...                   '\ndir2\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\t\t\tsubsubsubdir3\n\t\t\t\tfile3.ext')
    47
