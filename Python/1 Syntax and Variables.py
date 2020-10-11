print("hello don , wassgood")

if 5 > 2 :
 print("five is greater than 2")
 #indentation is very important in python to identify the different blocks otherwise it will give an error.
 #indentation is the space before your line of code.
 print("five is greater than 2")
#in the same block indentation should be the same, eg if you used one space at first for the second one you should also use on space.

x = 5
y = "Hello world"
#in python Variables are created when you assign a value to it, the is no declaration of variables in python
#declaring a variable is defining its type
# x is of type in and y is of type string

print(x)
print(y)
"""
This is a multiline comment python will read it and ignore it
wasssss goooooooddddddddddd

"""

#variables can even change type after they have been set.

myvar = 5
#the type here is int

myvar = "john paul"     #String variables can be decalared using either a single or double quote.
#the type is now a string
print(myvar)


"""
Naming variable in python
 > the variable name must start with a letter or underscore eg myvar , _myvar
 > A variable name can only contain alpha numeric characters and underscores (A-z,0-9, _)
 > Variable names cannot start with a number
 > Variable names are case sensitive eg dog , Dog
"""
#Assigning values to multiple Variables in one line

x,y,z = "This","is", "awesome"

print(x)
print(y)
print(z)

#Assigning a value to the same variables
s=r=t=" Stratizen "

print(s)
print(r)
print(t)
# output :  Stratizen Stratizen Stratizen

#Combining both text and Variables using the + operator

print("Hey there "+ r + " , the one and only one ")
# output : Hey there  Stratizen  , the one and only one

#adding a variable to another using the + operator

py = "python"
aw =  " is awesome ."
sum = py + aw

print(sum)
# output python is awesome


# For number the + works as the plus operator

num_1 = 4
num_2 = 5
num_3 = num_1 + num_2

print(num_3)
#output : 9

#if you try to combine a string and a number python will give you an error


"""
Global Variables :  They can be used both inside and outside functions
"""
# Global variables

Awee = "awesomest"

# keyword def is used to create user defined functions.

def myfunc():
 print("Python is "+ Awee) #Error experienced make sure the indent is in the block
myfunc()
#calling the function
#output : Python is awesomest

def myfunc1():
 Awee = "fantastic" #usable only inside the function
 print("Python is "+ Awee) #Error experienced make sure the indent is in the block
myfunc1()
#calling the function
#Output : Python is fantastic

"""
Using the Global keyword
"""

def myfunc2():
 global Awee1
 Awee1 = "fantasticaaaaa" #the global keyord makes the variable defined in the function available int he global scope

myfunc2()

print("This python is "+ Awee1)
#output : This python is fantasticaaaaa

Awee2 = "Brilliant" #normal global variable

def myfunc3():
 global Awee2
 Awee2 = "Brilliantesttttt"  #local variable using the global keyword
myfunc3()

print("Python is " + Awee2)
#output : Python is Brilliantesttttt
# the normal global variable was overriden by the variable in the function that used the global keyword
