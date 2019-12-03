def coding_problem_19(house_costs):
    """
    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
    while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and
    kth column represents the cost to build the nth house with kth color, return the minimum cost.
    Example:

    >>> house_size = [1, 2, 4, 2]  # size of the house
    >>> color_cost = [1, 2, 4]  # cost of paint for each color
    >>> house_costs = [[cc * hs for cc in color_cost] for hs in house_size]  # 4 houses, 3 colors
    >>> coding_problem_19(house_costs)  # [1,2,4,2] . [1,2,1,2] == 1*1 + 2*2 + 1*4 + 2*2 == 13
    13

    Notes: this is dynamic programming in disguise. We assign a color to each house in order, and keep
    track of the minimum cost associated with each choice of color. These costs are the minimum over all
    possible permutation in which the last added house is of a particular color.
    """
    best_costs = [0] * len(house_costs[0])
    for color_costs in house_costs:  # color_costs are those paid to paint last added house with a certain color
        best_costs = [color_costs[i] + min(best_costs[:i] + best_costs[i + 1:]) for i in range(len(best_costs))]

    return min(best_costs)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
