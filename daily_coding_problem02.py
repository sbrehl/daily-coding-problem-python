# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:49:56 2022

@author: Sascha

Daily Coding Problem #2 (Uber)

Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import numpy as np
import time

def array_product(original_array):
    '''
    makes a copy of the original_array, deletes the element at index i, and
    multiplies the remaining entries

    Parameters
    ----------
    original_array : array
        an array of numbers.

    Returns
    -------
    final_array : array
        an array of numbers where each element at index i is the product of all 
        the numbers in original_array except the one at index i.

    '''
    final_array = []
    
    for i in range(0, len(array)):
        temp_array = original_array[:]
        del temp_array[i]
        final_array.append(np.prod(temp_array))
        
    return final_array

# problem with big numbers: np.product calculates a float; loops back over

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

tic = time.perf_counter()
print(array_product(array))
toc = time.perf_counter()
print(f"Function array_product takes {toc - tic:0.7f} seconds to run")

#%% 

def without_numpy(original_array):
    '''
    Does the same as array_product, except that it uses a for-loop to calculate
    the product, rather than np.product

    Parameters
    ----------
    original_array : array
        an array of numbers.


    Returns
    -------
    final_array : array
        an array of numbers where each element at index i is the product of all 
        the numbers in original_array except the one at index i.

    '''
    final_array = []
    
    for i in range(0, len(array)):
        temp_array = original_array[:]
        del temp_array[i]
        
        product = 1
        for j in temp_array:
            product *= j
            
        final_array.append(product)
    
    return final_array

# faster and more accurate than array_product

tic = time.perf_counter()
print(without_numpy(array))
toc = time.perf_counter()
print(f"Function without_numpy takes {toc - tic:0.7f} seconds to run")
        