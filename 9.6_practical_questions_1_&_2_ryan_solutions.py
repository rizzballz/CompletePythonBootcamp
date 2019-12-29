# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
#class BankAccount(object):
#    ''' Bank Account Class.
#        
#        Attributes
#        -----------
#        acc_name = name of account
#        status = status of the bank account OPEN/CLOSED/INACTIVE
#        balance = Sum total of money held within the account
#    '''
#    
#    def __init__(self, balance=0.0):
#        self.status = 'OPEN'
#        self.balance = balance
#        
#    def withdraw(self, amount):
#        if amount > self.balance:
#            print('Insufficient balance')
#        else:
#            self.balance -= amount
#            print(f'You have withdrawn ${amount}.\n'\
#                  f'${self.balance} remaining')
#
#    def get_balance(self):
#        print(f'Your current balance is: ${self.balance}')
#        pass
#    
#    def deposit_money(self, amount):
#        self.balance += amount
#    
#ryan = BankAccount(50.0)
#ryan.get_balance()

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

class Circle(object):
    '''
    Circle class
    
    Attributes:
    -----------
    radius: float value of the radius of the circle
    diameter: float value of the diameter of the circle
    area: float value of the area of the circle
    circumference: float value of the Circumference of the circle
    '''
    # Constant for the value of pi
    PI = 3.14159
    
    def calculate_diameter(self, radius):
        ''' Return a float value of the diameter of the circle object '''
        return (radius*2)
    
    def calculate_area(self, pi, radius):
        ''' Return a float value of the area of the circle '''
        return(pi*radius**2)
    
    def __init__(self, radius=1.0):
        ''' Initialisation function. 
        Set radius equal to supplied value or 1 if not supplied.
        Call calculate_diameter() method to set diameter variable value
        Call calculate_area() method with supplied radius.'''
        self.radius = radius
        self.diameter = self.calculate_diameter(self.radius)
        self.area = self.calculate_area(self.PI, self.radius)
        
circle = Circle()