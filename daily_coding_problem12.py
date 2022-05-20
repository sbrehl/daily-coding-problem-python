# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:53:06 2022

@author: Sascha

Daily Coding Problem #12 (Amazon)

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5}, 
you could climb 1, 3, or 5 steps at a time.

"""

fib_dict = {}
# base cases
fib_dict[1] = 1 
fib_dict[2] = 2

def climb_stairs(number_of_steps):
    '''
    This function solves the case of 1 or 2 steps at a time.
    This basically follows the Fibonacci sequence, which is why I implemented
        a fast recursive version to calculate this sequence.

    Parameters
    ----------
    number_of_steps : integer
        the number of steps to be climbed.

    Returns
    -------
    integer
        number of possible combinations in which the steps can be climbed.

    '''
    global fib_dict
    # I set up a dictionary, in which the numbers of the fibonacci sequence can
    # be saved, so that they only have to be calculated once, and not multiple
    # times during recursion
    # also, by saving this dictionary in a global scope, all numbers can just
    # be looked up during future uses of the function
    if number_of_steps in fib_dict:
        return fib_dict[number_of_steps]
        # this part looks up the "number_of_steps"th fibonacci number in the
        # dictionary
    else: 
        fib_dict[number_of_steps] = climb_stairs(number_of_steps - 1) + climb_stairs(number_of_steps - 2)
        return fib_dict[number_of_steps]
        # recursion

#%%

def climb_stairs2(number_of_steps, steps_at_a_time):
    '''
    This function solves the problem for all possible sets of steps that can
    be taken at a time recursively.

    Parameters
    ----------
    number_of_steps : integer
        the number of steps to be climbed
    steps_at_a_time : list of integers
        the numbers of steps that can be taken at a time

    Returns
    -------
    integer
        number of possible combinations in which the steps can be climbed

    '''
    
    # base case
    if number_of_steps <= 1:
        return 1
    
    number_of_ways = 0
    
    for steps in steps_at_a_time:
        if number_of_steps >= steps:
            number_of_ways += climb_stairs2(number_of_steps - steps, steps_at_a_time)
    
    return number_of_ways