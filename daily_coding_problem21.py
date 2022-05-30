# -*- coding: utf-8 -*-
"""
Created on Mon May 30 07:41:37 2022

@author: Sascha

Daily Coding Problem #21 (Snapchat)

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from scipy.stats import mode
import time

def solution1(time_intervals):
    '''
    simple but inefficient
    
    the general idea is to include all times in which a room is occupied (e.g. 
        30, 31, 32, 33, 34, 35 for (30, 35)) in a list, repeat for every room,
        and find the amount of times the mode of this list occurs

    Parameters
    ----------
    time_intervals : list of tuples
        the start and end times for classroom lectures

    Returns
    -------
    required_classrooms : int
        the amount of required classrooms

    '''
    time_list = []
    
    for intervals in time_intervals:
        for times in range(intervals[0], intervals[1]):
            time_list.append(times)
    
    required_classrooms = mode(time_list).count[0]
    return(required_classrooms)

def solution2(time_intervals):
    '''
    

    Parameters
    ----------
    time_intervals : list of tuples
        the start and end times for classroom lectures

    Returns
    -------
    required_rooms : int
        the amount of required classrooms

    '''
    start_end = []
    
    for intervals in time_intervals:
        # writes all start and end times to a single list, together with a 1
        # for starting times (meaning that one extra room will be occupied) and
        # -1 for ending times (meaning that one extra room will be freed)
        start_end.append([intervals[0], 1])
        start_end.append([intervals[1], -1])
        
    start_end = sorted(start_end)
    
    current_rooms = 0
    required_rooms = 0
    
    for times in start_end:
        # counts the occupied rooms after any given start and ending time
        current_rooms += times[1]
        
        # ensures that the maximum number of current rooms is saved in 
        # required_rooms
        if current_rooms > required_rooms:
            required_rooms = current_rooms
            
    return required_rooms

time_intervals = [(30, 75), (0, 50), (60, 150), (10, 48), (45, 90), (100, 160)]

tic = time.perf_counter()
print(solution1(time_intervals))
toc = time.perf_counter()
print(f"Solution 1 takes {toc - tic:0.7f} seconds to run")

tic = time.perf_counter()
print(solution2(time_intervals))
toc = time.perf_counter()
print(f"Solution 2 takes {toc - tic:0.7f} seconds to run")