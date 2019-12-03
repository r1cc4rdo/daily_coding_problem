## Problem 19

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and
kth column represents the cost to build the nth house with kth color, return the minimum cost.

Example:

    >>> house_size = [1, 2, 4, 2]  # size of the house
    >>> color_cost = [1, 2, 4]  # cost of paint for each color
    >>> house_costs = [[cc * hs for cc in color_cost] for hs in house_size]  # 4 houses, 3 colors
    >>> coding_problem_19(house_costs)  # [1,2,4,2] . [1,2,1,2] == 1*1 + 2*2 + 1*4 + 2*2 == 13
    13
