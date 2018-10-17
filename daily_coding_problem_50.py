"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal 
node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

from nose.tools import assert_equal

tab = ['*', '+', '+', 3, 2, 4, 5]     # Storing the array as a table 

def eval(tab, i):
    op = tab[i]
    lft = left(i)
    rgt = right(i)
    if op == "+":
        return eval(tab, lft) + eval(tab, rgt)
    elif op == "-":
        return eval(tab, lft) - eval(tab, rgt)
    elif op == "*":
        return eval(tab, lft) * eval(tab, rgt)
    elif op == "/":
        return eval(tab, lft) / eval(tab, rgt)
    else: 
        return op
    
def left(i):
    return int(2*i + 1)
def right(i):
    return int(2*i + 2)

print(assert_equal(eval(['*', '+', 4, 5, 6], 0), 44))
print(assert_equal(eval(['*', 4, '+', ' ', ' ', 5, 6], 0), 44))
