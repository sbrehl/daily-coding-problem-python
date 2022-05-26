# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:58:31 2022

@author: Sascha

Daily Coding Problem #15 (Facebook)

Given a stream of elements too large to store in memory, pick a random element 
from the stream with uniform probability.
"""

import random

def generator(number_of_elements):
    for x in range(number_of_elements):
        yield x

def pick_element(sample_generator):
    current_number = 0
    picked_sample = None
    
    for current_sample in sample_generator:
        current_number += 1
        if random.random() <= 1 / current_number:
            picked_sample = current_sample
            
        # since we don't know the length of the stream beforehand, we have
        # to use some mathematical knowledge, to pick one element with uniform
        # probability
        # https://stackoverflow.com/questions/23351918/select-an-element-from-a-stream-with-uniform-distributed-probability
            
    return picked_sample

number_of_elements = 1234

print(pick_element(generator(number_of_elements)))