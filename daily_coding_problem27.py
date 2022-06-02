# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:52:46 2022

@author: Sascha

Daily Coding Problem #27 (Facebook)

Given a string of round, curly, and square open and closing brackets, return 
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def balanced(string):
    '''
    the general idea is to first save all opening brackets in order. when a
        closing bracket occurs, concatenate it with the last saved bracket, and
        check if the concatenated string is equal to "()", "[]" or "{}"

    Parameters
    ----------
    string : string
        a string of brackets, consisting of "()[]{}".

    Returns
    -------
    bool
        returns if the brackets are balanced.

    '''
    brackets = []
    
    while string:
        # after working on the current bracket, it is removed from string, so
        # if string is empty, we are done checking
        
        if string[0] == "(" or string[0] == "[" or string[0] == "{":
            brackets.append(string[0])
            string = string[1:]
            # if the current bracket is an opening bracket, it will be saved
            # in "brackets"
            
        if string[0] == ")" or string[0] == "]" or string[0] == "}":
            test_bracket = brackets[-1] + string[0]
            # if the current bracket is a closing bracket, it is concatenated
            # with the last saved opening bracket
            brackets.pop(-1)
            # the last saved bracket is deleted, so that the next closing bracket
            # will be matched to the right opening bracket
            string = string[1:]
            
            if test_bracket != "()" and test_bracket != "[]" and test_bracket != "{}":
                # if the concatenated string is not equal to "()" or "[]" or 
                # "{}", the brackets are not balanced, so return False
                return False
    
    if brackets:
        # if there are still opening brackets left in "brackets", the number
        # of opening and closing brackets is not evenly matched, so return False
        return False
    
    return True

string1 = "([])[]({})"
string2 = "([)]"
string3 = "((()"

print(balanced(string1))
print(balanced(string2))
print(balanced(string3))