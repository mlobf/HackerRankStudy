"""
Task
Given an integer,

If is odd 'impar', print Weird

Id is even'par' and inclusive range of 6 to 20, print,  Weird.
Id is even'par' and greatter than 20, print Not Weird.
Id is even'par' and inclusive range of 2 to 5, print, not Weird

Input format must be a single line containing a positive interger

"""


x = int(input('Put a positive number'))


if x % 2 != 0:
    print('Weird')
elif x in range(6, 20, 1):
    print('Weird')
elif x in range(2, 5, 1):
    print('not Weird')
elif x > 20:
    print('not Weird')
