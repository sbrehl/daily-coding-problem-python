# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:36:55 2022

@author: Sascha

Daily Coding Problem #46 (Amazon)

Given a string, find the longest palindromic contiguous substring. If there 
are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The 
longest palindromic substring of "bananas" is "anana".
"""

def palindromic_substring(string):
    '''
    this function takes a string, and finds the longest palindromic contiguous
    substring.
    it does so by checking an increasingly smaller sliding window

    Parameters
    ----------
    string : str
        the string to be tested for palindromes.

    Returns
    -------
    sub_str : str
        the longest palindromic contiguous substring.

    '''
    
    # this loop represents the size of the sliding window
    # it starts by checking if the whole word (len(string)) is a palindrome
    # and decreases by one in every iteration
    for sub_str_len in range(len(string), 0, -1):
        # this loop represents the position of the sliding window, it starts
        # at the first letter, and then slides over one position, as many times
        # as there are different windows for this word: 
        # (len(string) - sub_str_len) times
        for starting_point in range(len(string) - sub_str_len + 1):
            
            # the current substring to be checked
            sub_str = string[starting_point:starting_point + sub_str_len]
            
            # if the sub_str is equal to its inversion, we have a palindrome
            # and the function ends
            if sub_str == sub_str[::-1]:
                return sub_str
            
a = 'aabcdcb'
b = 'bananas'
c = 'aoisghakljghawelsfgdhwteweweipojtipracecarojgprojh'

print(palindromic_substring(a))
print(palindromic_substring(b))
print(palindromic_substring(c))