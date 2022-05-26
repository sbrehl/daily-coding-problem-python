# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:22:05 2022

@author: Sascha

Daily Coding Problem #16 (Twitter)

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be 
        smaller than or equal to N.

You should be as efficient with time and space as possible
"""

class order_storage(object):
    def __init__(self):         
        self.log = []     
    
    def record(self, order_id):
        self.log.append(order_id)
        
        if len(self.log) > N:
            self.log = self.log[1:]
        
    def get_last(self, i):
        return self.log[-i]

N = 5