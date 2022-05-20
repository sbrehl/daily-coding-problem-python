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
        
        if len(current_letters) >= dist_characters+1:
            
            current_substring = ''
            current_letters = []
                
            length_longest_substring = func_longest_substring(string[1:], dist_characters)
        current_substring += letter
        
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        
        if len(longest_substring) > length_longest_substring:
            length_longest_substring = len(longest_substring)
                
            
    return length_longest_substring

s = "abababcdefgabababababab"
k = 2

print(func_longest_substring(s,k))