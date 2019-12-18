#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}
            
#country = input("Enter the name of a country and ill try look it up.\n >>").capitalize()
#if country in capitals.keys():
#    print(f'{country} is in the dictionary, the capital city is {capitals[country]}')
#else:
#    print(f'{country} is not in the dictionary')

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
##Create two lists, x = range 1-12, y = the beginning of the fib sequence [0,1]
#x = list(range(1,13))
#y = [0,1]
#
##Finish off the FIbonnaci list by iterating over it 10 times, apppending the sum of the last 2 digits
#for i in range(len(x)-2):
#    y.append(y[i]+y[i+1])
#    
## Create a new dictionary using dictionary comprehension, zipping together list x and list y
#fib_dict = {k:v for (k,v) in zip(x,y)}
#print(fib_dict)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

##Store the data from the question as lists and list of lists.
#companies = ['Python DS','Pythonsoft', 'Pythazon','Pybook']
#key_names = ['Open','High','Low','Close']
#prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#          [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
##Create dictionary 
#share_dict = {}
#
##Iterate through this 4 times
#for i in range(len(key_names)):
#    #add ith 'company'key to the dictionary which contains a dictionary value comprised of keynames zipped with the ith price list.
#    share_dict[companies[i]] = dict(zip(key_names,prices[i]))
#    
#print(share_dict)
'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
#import pprint
#
#pprint.pprint(share_dict, compact=True)
#
#import math
#
#print('let\'s find the length of a hypotenuse in a right angled triangle')
#side1 = int(input('Enter first side integer'))
#side2 = int(input('Enter second side integer'))
#hypotenuse = math.hypot(side1,side2)
#print(f'the length of the hypotenuse is: {hypotenuse}')

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
#import string
#from random import randint
#import matplotlib.pyplot as plt
#
#letters = [x for x in string.ascii_uppercase]
#vals = [randint(1,100) for x in range(len(letters))]
#
#d_1 = {k:v for (k,v) in zip(letters,vals)}
#
#x,y = zip(*d_1.items())
#plt.bar(x,y)



'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
suits = ['Hearts','Diamonds','Spades','Clubs']
values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

deck = {}

for i in range(len(suits)):
    deck[suits[i]] = values
    
print(deck)
    