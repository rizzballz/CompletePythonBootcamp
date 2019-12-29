#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:22:12 2019

@title: two_sum_ryan_solution.py
@author: Ryan McMillan

"""

def two_sum(nums,target):
    '''
    Return the index numbers of two integers that add up to a target number else 
    return -1
    '''
    
    # Counter to be used as the index of the first number to return.
    first = 0
    
    # Iterate through all of the numbers (num) in the list (nums).
    for num in nums:
        # The difference (dif) between num and target is what we need to find.
        dif = target - num
        # If the difference (dif) is in nums list
        if dif in nums:
            # What is the index location of the difference
            second = nums.index(dif)
            # Ensure that we are not looking at the same number twice ie:
            # target = 10 index of 5 in the list dif will also equal 5
            if first != second:
                # If numbers are different return a tuple
                return first, second
        # If difference not in nums increase first counter
        first += 1
    # The required number is not in the list return -1
    return -1
            


print(two_sum([1,2,5,4,6], 10))
print(two_sum([1,2,3,4,5], 8))
print(two_sum([1,2,3,4,5], 23))
    