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

    # def __rpr__(self):
    #     '''
    #     docstring
    #     '''
    #     return self.stack

    def push(self, item):
        '''
        Push an item to the top of the stack.
        '''
        self.stack.append(item)

    def pull(self, item):
        '''
        Pull the top item from the stack. Item is removed.
        '''
        return self.stack.pop()

    def peek(self):
        '''
        Look at the top item on the stack but do not remove it.
        '''
        return self.stack[-1]

stack = Stack()
stack.push(1)
stack.push(3)
print(stack.peek())
