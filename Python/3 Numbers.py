import random
"""
The numeric types in python are
Int
float
complex
"""
#Int
""" These are whole numbers either positive or negative , without decimal points , of unlimited length"""
x = 1
print(type(x))  #output : <class 'int'>


#float
"""
This is a number potivite or negative containing one or more decimal points
floats can also be scientific numbers with an e to indicate to the power of 10
"""
y = 2.1
yTwo= 4e3

print(type(y))      #output : <class 'float'>
print(type(yTwo))   #output: <class 'float'>
print(yTwo)         #output : 4000.0


#Complex
"""
complex number are written with a j as the imaginary part
"""
z = 3j
print(type(z))  #output : <class 'complex'>


'''
Type conversions with the int(), float(),complex() methods
'''

a = float(x)    # converting x which is an int to a float
print(type(a))  # ouput : <class 'float'>

b = int(y)      # Converting y which was of type float to an int type
print(type(b))  # output : <class 'int'>

c = complex(x)  # Converting x which is a integer to a complex
print(type(c))  # output : <class 'complex'> nb -> you cannot convert a complex type to any other type


'''
Random numbers
Python doesnt have the Random() function to make a randon number,
but python has a built in module called random that can be used to make random number

import random #importing the random module
'''

print(random.randrange(1,10))   #Display a random number between 1 and 9
