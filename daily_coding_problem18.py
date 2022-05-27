# -*- coding: utf-8 -*-
"""
Created on Fri May 27 07:44:34 2022

@author: Sascha

Daily Coding Problem #18 (Google)

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: 
[10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place 
and you do not need to store the results. You can simply print them out as you 
compute them.
"""

def max_of_subarray(array, k):
    length_of_array = len(array)
    
    # the number of windows to be considered. If, like in the example, the array
    # has 6 entries, and k = 3, then we need to consider 6 - 3 + 1 = 4 different
    # combinations of array entries
    number_of_subarrays = length_of_array - k + 1
    
    for number in range(number_of_subarrays):
        print(max(array[number:number+k]))
        
array = [10, 5, 2, 7, 8, 7]
k = 3

max_of_subarray(array,k)

# O(n) time, but not O(k) space

from collections import deque

def deque_implementation(array, k):
    '''
    reference: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

    Parameters
    ----------
    array : array
        the input array, of which the function should print the maximum in each
            window of k elements.
    k : int
        the size of the window of entries in the array to be considered.

    Returns
    -------
    prints the maximum value of each sliding window

    '''
    queue = deque()
    # queue: a linear data structure that follows a particular order in which
    # the operations are performed for storing data
    # dequeue: a type of queue that is double ended. elements can be inserted
    # and removed from both ends
    
    for index in range(k):
        # this loop builds up the queue with the first sliding window of elements
        
        # if the element to be added is bigger than the one that is already
        # stored in the queue, the stored ones can be removed
        while queue and array[index] >= array[queue[-1]]:
            queue.pop()
            
        queue.append(index)
        
    length_of_array = len(array)
    
    for index in range(k, length_of_array):
        # this loop deals with the rest of the elements; those elements not
        # in the first sliding window
        
        # prints the element of the front of the queue, which should at this
        # point be the largest element of the previous sliding window
        print(array[queue[0]])
        
        while queue and queue[0] <= index - k:
            # removes all of the elements which are not in the current window
            # from the front of the queue
            queue.popleft()
            
        while queue and array[index] >= array[queue[-1]]:
            # removes all elements that are smaller than the element being added
            # at this loop
            queue.pop()
            
        # adds current element at the rear of the queue    
        queue.append(index)
    
    # prints the maximum of the last window
    print(array[queue[0]])
    
deque_implementation(array, k)    