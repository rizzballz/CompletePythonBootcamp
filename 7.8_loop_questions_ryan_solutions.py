#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Completed 17 Dec 2019

@author: Ryan McMillan
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
#inputs = []
#inputs.append(int(input("Enter a number between 1 and 100:\n >>")))
#inputs.append(int(input("Enter a second number between 1 and 100:\n >>")))
#
#for i in range(min(inputs),max(inputs)+1,1):
#    print(i)

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
#string = input("Enter some text:\n >>")
#rev_string = []
#for char in string:
#    rev_string.insert(0, char)
#    
#print(''.join(rev_string))


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
#number = int(input("Enter a number between 1-12:\n >>"))
#
#if number in range(1,13):
#    for x in range(1,13):
#        print(f'{x} x {number} = ' + str(x*number).rjust(1))

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
#for x in range(1,13):
#    if x != 1:
#        print()
#    for y in range(1,13):
#        print(f'{x} x {y} = ' + str(x*y).rjust(1))

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
#import statistics
#
#inputs = []
#
#while -1 not in inputs:
#    inputs.append(int(input('Enter a number, type -1 to exit.')))
#
#inputs.remove(-1)  
#print('The average is', statistics.mean(inputs))

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

#'''Using recursion '''
#def n_factorial(n):
#    if n ==1:
#        return n #1 factorial is 1*1=1
#    else:
#        return n*n_factorial(n-1) #if the answer is not yet 1, current number(n) go into this method again using current number(n)-1
#    
#print(n_factorial(15))

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

#fib_nums = []
#
#for x in range(0,20):
#    if x == 0:
#        fib_nums.append(0)
#    elif x == 1:
#        fib_nums.append(1)
#    else:
#        fib_nums.append(fib_nums[-2]+fib_nums[-1])
#        
#print(fib_nums)

'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
#The solution code is below.
print('\t',5*'*','\n\t *\n\t',4*'*','\n',3*'\t *\n')


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
odd = []
even = []

for i in range(1,101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(odd)
print(even)