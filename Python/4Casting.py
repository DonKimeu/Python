'''
Casting in Python
> casting in python can be used when you want to declare a type on a variable
> Python is an object oriented language and as such it uses classes to define data types

Casting in python can be done using Constructor functions
int() - constructs an integer
        from a float it rounds of to the nearest whole number
        from a string it converts it to an integer value

float() - constructs a float number

str() - constructs a string from a wide variety of data types
'''



'''-------------------------int() function-------------------------'''

first = int(5)  # The type if first is an integer therefore no conversion will be done
print(first)    # output : 5
print(type(first))# output : <class 'int'>

a = int(2.8)    # The function int will convert the value of a to the nearest integer value
print(a)        # output : 2
print(type(a))  # output : <class 'int'>

b = int("4")    # The value of b is in the form of a String and will be converted by the int() function
print(b)        # output : 4
print(type(b))  # output : <class 'int'>



'''-------------------------float() function-------------------------'''

c = float(1)    # The value of c is of type int and will be converted to type float
print(c)        # output : 1.0
print(type(c))  # output : <class 'float'>

d = float(2.8)  # The value of d is of type float therefore no conversion will be done
print(d)        # output : 2.8
print(type(d))  # output : <class 'float'>

e = float("2.2")# The value of e is of type string therefore it will be converted to type float
print(e)        # output : 2.2
print(type(e))  # output : <class 'float'>



'''-------------------------str() function-------------------------'''

f = str("45")   # The value of f is already of type string therefore no changes will be made
print(f)        # output : 45
print(type(f))  # output : <class 'str'>

g = str(8)      # The value of g is of type int therefore it will be converted to a string
print(g)        # output : 8
print(type(g))  # output : <class 'str'>

h = str(3.0)    # The value of h is of type float therefore it will be converted to a string
print(h)        # output : 3.0
print(type(h))  # output : <class 'str'>
