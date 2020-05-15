'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

#_________________________________________________________

def missing_int(l):
    l = sorted([x for x in l if x > 0])  # removing all non-positive integers (i.e. negative integers including zero), as positve integer is to be found.
    for i in range(0, len(l)-1):
        if l[i] != l[i+1] and l[i] != l[i+1]-1: return l[i] + 1
    else: return l[-1] + 1

print(missing_int(eval(input())))
