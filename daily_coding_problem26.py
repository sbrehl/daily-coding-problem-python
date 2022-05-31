# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:23:53 2022

@author: Sascha

Daily Coding Problem #26 (Google)

Given a singly linked list and an integer k, remove the kth last element from 
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def insert_at_front(self, value):
        node = Node(value)
        
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def insert_at_back(self, value):
        node = Node(value)
        
        if self.is_empty():
            self.head = node
        else:
            curr = self.head 
            
            while curr.next != None:
                curr = curr.next
            curr.next = node
            
    def remove_element(self, position):
        '''
        This incorporates the method of two pointers.
            Because we should only go through the linked list once, it is not
            possible to know how long it is going to be beforehand. To solve
            this, we create two pointers, one of which is "position" steps 
            ahead of the other. If the pointer which is ahead reaches the end
            of the list, the second pointer is exactly "position" steps away
            from the end of the list, exactly at the node which should be
            deleted.

        Parameters
        ----------
        position : integer
            the position of the node which should be deleted, counting from
                the end of the list.

        Returns
        -------
        None.

        '''
        
        leading_pointer = self.head
        trailing_pointer = self.head
        
        for _ in range(position):
            leading_pointer = leading_pointer.next
        
        while leading_pointer.next != None:
            leading_pointer = leading_pointer.next
            trailing_pointer = trailing_pointer.next
        
        # to delete an element from the linked list, simply make the previous
        # node point to the node after the current node
        trailing_pointer.next = trailing_pointer.next.next
            
list1 = LinkedList()
list2 = LinkedList()
list1.insert_at_front(1)
list1.insert_at_back(5)
list1.insert_at_back(10)

list2.insert_at_front(9)
list2.insert_at_back(5)
list2.insert_at_back(10)

list1.remove_element(2)