#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:59:03 2020

@author: Ryan McMillan
@title: Stacks
@description: Create a program that checks for balanced parenthesis, 
    brackets and braces (), [], {}. Use stacks to do this.
    Create a stack class to handle the stack object
"""

class Stack(object):
    '''
    Stack class to describe a Stack object. Similar to a list in that 
    you can pop from the top (pull), append to the end of the stack 
    (push).

    Attributes:
    -----------
    stack = The list of items
    '''
    def __init__(self):
        '''
        On instantiation, initialise an empty list (stack).
        '''
        self.stack = []

    def add_to_stack(self, item_string):
        '''
        take a string of characters and push each individual item from the string to the stack.
        '''
        for item in item_string:
            self.push(item)

    def is_empty(self):
        '''
        Check to see is the stack is empty return True if empty
        return False if items in stack.
        '''
        if not self.stack:
            return True
        else:
            return False

    def __repr__(self):
        '''
        Returns a representation of itself in the form of a list rather than
        <__main__.Stack object at 0x7efe521920d0>.
        '''
        return  repr(self.stack)

    def push(self, item):
        '''
        Push an item to the top of the stack.
        '''
        self.stack.append(item)

    def pull(self):
        '''
        Pull the top item from the stack. Item is removed.
        '''
        return self.stack.pop()

    def peek(self):
        '''
        Look at the top item on the stack but do not remove it.
        '''
        if self.stack == []:
            return None
        else:
            return self.stack[-1]


stack = Stack()
print(stack)
print(len(stack.stack))
