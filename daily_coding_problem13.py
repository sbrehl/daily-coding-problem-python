# -*- coding: utf-8 -*-
"""
Created on Fri May 20 08:22:18 2022

@author: Sascha

Daily Coding Problem #13 (Amazon)

Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

def func_longest_substring(string, dist_characters):
    current_substring = ''
    longest_substring = ''
    current_letters = []
    length_longest_substring = dist_characters
    
    for letter in string:
        if letter not in current_letters:
            current_letters.append(letter)
            
            # current_letters is my way of checking how many distinct characters
            # are already in use in the current substring
        
        if len(current_letters) >= dist_characters+1:
            
            current_substring = ''
            current_letters = []
            
            # if the length of current_letters exceeds the number of distinct 
            # characters that should occur, current_substring is deleted, so
            # so that it can be build up again without skipping the current letter
                
            length_longest_substring = func_longest_substring(string[1:], dist_characters)
            
            # the function is called recursively, with the first letter missing,
            # so that no possible combination of letters is missed. If the loop
            # were to simply go on, all the letters that were already looped over
            # would be disregarded, and the algorithm would have "missed" a
            # possible start of the longest substring
            
        current_substring += letter
        
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        
        if len(longest_substring) > length_longest_substring:
            length_longest_substring = len(longest_substring)
                
            
    return length_longest_substring