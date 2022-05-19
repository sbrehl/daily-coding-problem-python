# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:19:14 2022

@author: Sascha

Daily Coding Problem 4 (Stripe)

Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should 
give 3.

You can modify the input array in-place.
"""

def find_integer(array):
    
    if len(array) > 0:
        maximum = max(array)
    else:
        # if the array has a length of 0, 1 is the first positive integer
        # that is missing, and is therefore returned
        return 1
    
    if maximum < 1:
        # if there are no numbers greater than 0, 1 is the first positive
        # integer that is missing, and is therefore returned
        # this is handled as a fringe case, because the code would run into
        # problems otherwise
        return 1
    
    array.sort()
    
    for i in range(1, (maximum + 2)):
        # loops over all positive integers up to the maximum of the array, and
        # checks for each one if they are present. if an integer is not present,
        # the function returns that integer
        # the loop runs to maximum + 2, so that, if there are no gaps in the 
        # range of positive integers of the array, the highest number +1 gets 
        # included and returned
        if i not in array:
            return i
        
    return False
    # this should not occur, in theory. if it does, something is wrong with the
    # code
    
array = [-3,-2]
print(find_integer(array))

array2 = [1,2,3,4,5,6,8,9]
print(find_integer(array2))