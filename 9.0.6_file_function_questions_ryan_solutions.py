# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019
Answered on Wed Dec 18 20:04:00 2019

@author:    Giles
@student:   Ryan McMillan
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''

#def sum_two(a,b):
#    '''Takes two integers and returns their sum'''
#    return(a + b)
#    
#sum_two(5,5)

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''
#
#def multiply(x,y = 2):
#    return(x*y)
#
#print(multiply(2))
#print(multiply(2,3))

'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''
#
#def power(a,b=2):
#    return pow(a,b)
#
#print(power(3))
#print(power(2,3))

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''
#cap_cities = ['Sydney','Canberra','Perth','Hobart','Melbourne','Adelaide',
#              'Darwin','Brisbane']
#
#with open('capitals.txt','w') as f:
#    for x in range(len(cap_cities)):
#        f.write(cap_cities[x] + ' ')
    


'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''
#with open ('capitals.txt','a') as f:
#    f.write(input("Enter a new Capital City.\n >>"))
    
'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''
def copy(file_a, file_b):
    with open(file_a, 'r') as f:
        text = f.read()
        with open(file_b, 'w') as g:
            g.write(text)

copy('capitals.txt', 'capitals_2.txt')