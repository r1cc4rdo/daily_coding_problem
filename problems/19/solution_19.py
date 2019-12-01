def coding_problem_19(costs):
    """
    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
    while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and
    kth column represents the cost to build the nth house with kth color, return the minimum cost.
    """
    best_cost = [0] * len(costs[0])
    for cost in costs:  # add a house at a time
        for index in xrange(len(cost)):  # best cost is the one for that color plus min cost between every other color
            best_cost[index] = cost[index] + min(best_cost[:index] + best_cost[index + 1:])

    return min(best_cost)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
