# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:53:36 2022

@author: Sascha
"""

# Daily Coding Problem #45 (Two Sigma)

# Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
# with uniform probability, implement a function rand7() that returns an 
# integer from 1 to 7 (inclusive).

import random 
import numpy as np
from matplotlib import pyplot as plt

def rand5():
    return random.randint(1,5)

# first try
# something with z-transformation
# does not work out, since there are still only 5 possibly achievable numbers

def rand7():
    number = rand5()
    array5 = list(range(1,5+1))
    z = (number - np.mean(array5)) / np.std(array5)
    
    array7 = list(range(1,7+1))
    new_rnd = z * np.std(array7) + np.mean(array7)
    
    return new_rnd

# second try
# still does not achieve uniform distribution, because the chance for e.g. a
# 7 is only at 1/5  * 1/14, for a 6 only at 1/5 * 1/7

def rand7_2():
    number = rand5()
    
    random_number = random.random()
    if random_number < 1 / 7 / 2:
        number += 2
    elif random_number < 1 / 7:
        number += 1
        
    return number

# third try
def rand7_3():
    number = rand5()
    
    random_number = random.random()
    if random_number < 1/7:
        number = 6
    elif random_number > 6/7:
        number = 7

    return number

# check
numbers = [0] * 7000

for i in range(1,len(numbers)):
    numbers[i] = rand7_3()
    
plt.hist(numbers)
    