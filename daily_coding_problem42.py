# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:44:41 2022

@author: Sascha

Daily Coding Problem #42 (Google)

Given a list of integers S and a target number k, write a function that returns 
a subset of S that adds up to k. If such a subset cannot be made, then return 
null.

Integers can appear more than once in the list. You may assume all numbers in 
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
since it sums up to 24.
"""

S = [12, 1, 61, 5, 9, 2]
k = 24

# taken from Daily Coding Problem #37
def create_power_set3(original_set):
    '''
    The general idea is to create all possible subsets of the first entry, and
    add these to the list, already initiated with an empty list. The next step
    is then to consider all possible subsets of the set, also considering the
    next entry, and only those containing the next entry, add these to the list 
    and so on.

    Parameters
    ----------
    original_set : set
        a set of random entries.

    Returns
    -------
    power_set : list
        every possible combination of entries in original_set.

    '''
    power_set = [[]]
    
    for entry in original_set:
        # every entry in the original set is considered individually
        
        temp_set = []
        for subset in power_set:
            # this loop takes every value so far in the power_set, appends the 
            # current entry in original_set to this, and then appends this to
            # a temporary list
            # example:  current entry of original_set: 2
            #           entries in power_set so far: [], [1]
            # 1st loop: [] + [2] = [2]
            # 2nd loop: [1] + [2] = [1,2]
            # both of these are added to the power_set
            # new power set: [], [1], [2], [1,2]
            # the next outer loop then considers the 3, and so on
            temp_set.append(subset + [entry])
        power_set.extend(temp_set)
    return power_set

def subset_summation(list_of_integers, target_number):
    power_set = create_power_set3(list_of_integers)
    
    for subset in power_set:
        if sum(subset) == target_number:
            return subset
        
print(subset_summation(S,k))   