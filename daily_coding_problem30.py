# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:57:28 2022

@author: Sascha

Daily Coding Problem #30 (Facebook)

You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall and the 
integer is the height. Suppose it will rain and all spots between two walls get 
filled up.

Compute how many units of water remain trapped on the map in O(N) time and 
O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the 
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 
in the second, and 3 in the fourth index (we cannot hold 5 since it would run 
off to the left), so we can trap 8 units of water.
"""

def units_of_water(elevation_map):
    '''
    

    Parameters
    ----------
    elevation_map : list
        a list of integers, representing a two-dimensional elevation map, where
            each element is a unit-width-wall and the integer is the height.

    Returns
    -------
    final_units : int
        the amount of water that would be trapped between the walls in 
            elevation_map.

    '''
    
    left = 0
    width = 0
    current_units = 0
    final_units = 0
    
    for height in elevation_map:
        if height >= left:
            # if the elevation of the newly considered wall is higher than the
            # elevation of the current left wall, then we have a finished water
            # basin, and can add the amount of water which is trapped therein,
            # to the final count
            # the current wall is then set to be the new left wall, and the 
            # calculation for the new water basin begins
            
            final_units += current_units
            current_units = 0
            width = 0
            left = height
        else:
            # if the elevation of the current wall is lower than that of the
            # left wall, we are in the middle of a water basin, and can add the
            # difference in height to the amount of water in the current basin.
            current_units += left - height
            width += 1
    
    # in the case (not considered in the examples given in the problem) that
    # the right-most wall is not the highest, the amount of water that is
    # calculated within the loop is too high, because the loop only considers
    # the case where the water level is limited by the left wall.
    # to fix this, when the loop is done, current_units is reduced by the
    # amount of water that would flow out.
    # if all of the water flowed out, current_units would be smaller than or
    # equal to zero, so final_units would be unchanged
    current_units -= (left - height) * width
    
    if current_units > 0:
        final_units += current_units
        
    return final_units

map1 = [2, 1, 2]
map2 = [3, 0, 1, 3, 0, 5]
map3 = [3, 0, 1, 3, 0, 5, 4, 3, 2, 1]
map4 = [5, 0, 0, 3]

print(units_of_water(map1))
print(units_of_water(map2))
print(units_of_water(map3))
print(units_of_water(map4))