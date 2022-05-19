# -*- coding: utf-8 -*-
"""
Created on Thu May 12 07:44:42 2022

@author: Sascha

Daily Coding Problem #9 (Airbnb)

Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
import math

def largest_sum(list_of_integers):
    number_of_entries = len(list_of_integers)
    
    list_with_indices = [(index, item) for index, item in enumerate(list_of_integers)]
    # turns the original list of integers, into a list of tuples, with (index, integer)
    
    sorted_list = sorted(list_with_indices, key = lambda item: item[1], reverse = True)
    
    sums = [0] * number_of_entries
    indices = [None] * number_of_entries
    
    for i in range(0, len(sorted_list)):
        # the general idea is that of a greedy algorithm, which puts the biggest
        # integer into the sum, and then looks if the second-biggest can be added,
        # under the condition, that its index is not adjacent to that of any
        # number that has already been added
        
        sums[i] += sorted_list[i][1]
        # initializes the sum of the current loop with the number at the i-th 
        # position of the list
        indices[i] = [sorted_list[i][0]]
        # initializes the list of indices of the numbers that have are being
        # summed up
        
        for j in sorted_list:
            # loops over all the numbers, and looks if they can be added
            if j[0] not in indices[i] and j[0] + 1 not in indices[i] and j[0] - 1 not in indices[i] and j[1] > 0:
            # checks if the current number has already been added, or is adjacent
            # to a number that has already been added, and that it is positive
            # if not, it adds the current number to the sum, and appends the 
            # index
                sums[i] += j[1]
                indices[i].append(j[0])
        
    return max(sums)
    
a = [-100,-50,30,20,100,-50,-40,20]

print(largest_sum(a))
