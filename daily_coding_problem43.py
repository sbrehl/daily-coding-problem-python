# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:04:09 2022

@author: Sascha

Daily Coding Problem #43 (Amazon)

Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. 
        If there are no elements in the stack, then it should throw an 
        error or return null.
    max(), which returns the maximum value in the stack currently. 
        If there are no elements in the stack, then it should throw an 
        error or return null.

Each method should run in constant time.
"""

class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0
        
    def push(self, val):
        self.elements.append(val)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return None
        
        temp = self.elements[-1]
        self.elements.remove(self.elements[-1])
        self.size -= 1
        return temp
    
    def max(self):
        if self.size == 0:
            return None
        
        max_value = 0
        for i in self.elements:
            if i > max_value:
                max_value = i
                
        return max_value
    
ck = Stack()
print(ck.size)
ck.pop()
ck.max()
ck.push(1)
ck.push(3)
ck.push(2)
ck.pop()
ck.max()
