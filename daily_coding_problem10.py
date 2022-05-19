# -*- coding: utf-8 -*-
"""
Created on Thu May 19 07:49:51 2022

@author: Sascha

Daily Coding Problem #10 (Apple)

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds
"""
import time

def jobScheduler(function, waiting_time):
    '''
    Parameters
    ----------
    function : function
        the function to be delayed by waiting_time milliseconds
    waiting_time : int
        the time in milliseconds, for which the function should be delayed by

    Returns
    -------
    function : function
        the function to be delayed by waiting_time milliseconds

    '''
    # since time.sleep works with seconds instead of milliseconds, the time
    # has to be divided by 1000
    time.sleep((waiting_time / 1000))
    return function
