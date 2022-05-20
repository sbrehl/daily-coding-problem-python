# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:58:54 2022

@author: Sascha

# 1 Google

Given a list of numbers and a number k , return whether any two numbers from 
the list add up to k .

For example, given [10, 15, 3, 7] and k of 17 , return true since 10 + 7 is 17.
"""

# general note: both solutions run into problems when a certain number
# occurs twice in list_of_numbers

import time

def addition(list_of_numbers, sum_k):
    '''
    A brute force solution, which just performs addition on all possible
        combinations of numbers in list_of_numbers, and checks if they equal
        to sum_k.
    
    Parameters
    ----------
    list_of_numbers : list
        A list of numbers. Is checked for the occurence of two numbers which
        would add up to sum_k
        
    sum_k : int
        The integer which two numbers of list_of_numbers should add up to.

    Returns
    -------
    bool
        returns True if two numbers of list_of_numbers add up to sum_k
        returns False if sum_k can not be calculated through addition of two
            numbers from list_of_numbers

    '''
    for i in list_of_numbers:
        for j in list_of_numbers:
            # loops through all possible pairs of numbers, seeing if they
            # add up to sum_k
            if i + j == sum_k and i != j:
                # i != j skips the case where a number is added to itself
                return True
    return False

def difference(list_of_numbers, sum_k):
    '''
    

    Parameters
    ----------
    A smarter solution with faster runtime, which checks if the difference of
        sum_k and a given number in list_of_numbers occurs anywhere in 
        list_of_numbers.
    
    list_of_numbers : list
        A list of numbers. Is checked for the occurence of two numbers which
        would add up to sum_k
    sum_k : int
        The integer which two numbers of list_of_numbers should add up to.

    Returns
    -------
    bool
        returns True if two numbers of list_of_numbers add up to sum_k
        returns False if sum_k can not be calculated through addition of two
            numbers from list_of_numbers

    '''
    for i in list_of_numbers:
        # checks if the difference of sum_k and the current number to be
        # evaluated occurs in list_of_numbers.
        # if it does than there exists a pair of numbers where number + number
        # = sum_k, which satisfies the condition given by the problem
        if sum_k - i in list_of_numbers and (sum_k - i) != i:
            # (sum_k - i) != i skips the case of the two numbers being the same
            return True
    return False


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
k = 40

tic = time.perf_counter()
print(addition(a,k))
toc = time.perf_counter()
print(f"Function addition takes {toc - tic:0.7f} seconds to run")

tic = time.perf_counter()
print(difference(a,k))
toc = time.perf_counter()
print(f"Function difference takes {toc - tic:0.7f} seconds to run")