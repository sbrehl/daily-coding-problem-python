# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:01:04 2022

@author: Sascha

Daily Coding Problem #33 (Microsoft)

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of 
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two 
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should 
print out:

2
1.5
2
3.5
2
2
2

"""
import math

def running_median(sequence):
    '''
    This function computes the running median of a sequence of numbers

    Parameters
    ----------
    sequence : list
        a list of numbers.

    Returns
    -------
    int or float
        the median

    '''
    list_of_numbers = []
    
    for number in sequence:
        list_of_numbers.append(number)
        list_of_numbers.sort()
        
        if len(list_of_numbers) % 2 == 1:
            median = list_of_numbers[int(len(list_of_numbers) / 2)]
            # int() is for this purpose the same as rounding down
        else:
            median = (list_of_numbers[int(len(list_of_numbers) / 2)] +
                     list_of_numbers[int((len(list_of_numbers) / 2) - 1)]) / 2
        # print(list_of_numbers)    
        print(median)

numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [1,3,5,7,9,2,4,6,8,10]
numbers3 = [2,1,5,7,2,0,5]

running_median(numbers1)
running_median(numbers2)
running_median(numbers3)