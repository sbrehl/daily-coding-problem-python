# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:24:34 2022

@author: Sascha

Daily Coding Problem #14 (Google)

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a 
Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random
import math

def MonteCarlo(num_Trials):
    points_in_circle = 0
    for points in range(1, num_Trials + 1):
        x = random.random()
        y = random.random()
        
        # the idea is to randomly drop points in an square that is two times two
        # units of length. within which lies a circle with radius 1. if the point
        # is within 1 unit of length of the origin; it lies within the circle, if
        # not, it doesn't
        
        if math.sqrt(x*x + y*y) <= 1.0:
            points_in_circle += 1
        
        # the ratio of needles in the circle versus needles outside of the circle
        # should be the same as the ratio of the area of the circle versus the 
        # area of the square. the area of the circle would give us pi, since it
        # has a radius of 1.
        
        # needles in circle / needles in square = area of circle / area of square
        # area of circle = (area of square * needles in circle) / needles in square
        # sub in 2*2 = 4 for area of square
        # area of circle = (4 * needles in circle) / needles in square
        
    pi_estimate = 4 * (points_in_circle / num_Trials)
    pi_estimate = round(pi_estimate, 3)
    
    return pi_estimate