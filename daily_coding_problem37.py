# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:31:52 2022

@author: Sascha

Daily Coding Problem #37 (Google)

The power set of a set is the set of all its subsets. Write a function that, 
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return 
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


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

original_set = {1, 2, 3}
        
print(create_power_set3(original_set))
