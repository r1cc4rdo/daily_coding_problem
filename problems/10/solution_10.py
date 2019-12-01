def coding_problem_10():
    """
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    Example:

    >>> coding_problem_10()
    Before
    Hello from thread
    After
    """
    from threading import Thread
    import time

    def delayed_execution(f, ms):
        time.sleep(ms)
        return f()

    def hello(name):
        print 'Hello {}'.format(name)

    job = Thread(target=delayed_execution, args=(lambda: hello('from thread'), 0.01))
    job.start()

    print 'Before'
    time.sleep(0.02)
    print 'After'


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)