import random


def coding_problem_15(sample_generator):
    """
    Given a stream of elements too large to store in memory, pick a random element from the stream with
    uniform probability.
    Example:

    >>> import random
    >>> random.seed(0xBADC0FFE)

    >>> def sample_gen_fun(n):
    ...     for x in xrange(n):
    ...         yield x

    >>> num = 10
    >>> hist = [0] * num
    >>> for trials in xrange(5000):
    ...     hist[coding_problem_15(sample_gen_fun(num))] += 1

    >>> all(abs(float(h) / sum(hist) - 1.0 / len(hist)) < 0.01 for h in hist)
    True

    Note: this problem only makes sense if you don't know the total number in advance. Otherwise, you would pick a
    random integer between [0..len[ and record the element corresponding to that index when processed. Setting a seed
    for the random number generator to avoid random failures due to unlucky distributions of samples.

    Strategy: assuming that at round n we have already selected between the available samples with uniform
    probability, accept the incoming one as the new selected sample with a probability that keeps everyone's chances
    fair. Example: at n==1, the first sample as 100% chance of being selected. n==2, second sample 50% chance, n==3
    1/3 chance etc. Proof: for n==5, the prob. of choosing first sample is 1 * 0.5 * 0.666.. * 0.75 * 0.8 = 0.2 = 1/5
    """
    sample_count = 0
    selected_sample = None
    for sample in sample_generator:

        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample

    return selected_sample


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
