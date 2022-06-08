# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 07:58:38 2022

@author: Sascha

Daily Coding Problem #36 (Dropbox)

Given the root to a binary search tree, find the second largest node in the tree.
"""
import numpy as np
import random

class Node:
    def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
      
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                 if self.right is None:
                     self.right = Node(data)
                 else:
                     self.right.insert(data)
        else:
            self.data = data

    def Traversal(self, root):
        vals = []
        
        if root:
            vals = self.Traversal(root.left)
            vals.append(root.data)
            vals = vals + self.Traversal(root.right)
        
        return vals
    
    def second_largest_node(self, vals):
        # since, during a normal Traversal (no matter which order) of a binary
        # tree, we can choose to store the values instead of printing them, we
        # can just sort these values and print out the second-largest one
        vals.sort()
        return vals[-2]
   
root = Node(10)
tree_vals = [10]

for i in range(6):
    number = random.randint(1,20)
    root.insert(number)
    tree_vals.append(number)
    
print(root.second_largest_node(root.Traversal(root)))

    