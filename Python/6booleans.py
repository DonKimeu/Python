'''
Booleans
booleans represent one of two values , True or False
You can evaluate any expression in python
'''

# When you compare two values the expression is evaluated and python returns the Boolean answer

print(10 > 9)     # Output : True
print(10 < 9)     # Output : False

# Performing an action in regard to whether the condition is true or False
a = 100
b = 300

if a > b :
    print("A is greater than B")
else :
    print("B is greater than A")
                # Output : B is greater that A


"""
Evaluate Values and Variables
The bool() function allows you to evaluate any value and give you a True or False answer in return

Most Values are evaluated as True
Any string is True except empty Strings
Any number is True except 0
Any list, tuple , set and dictionary are True except empty ones
"""
print(bool("Hello"))    # Output : True
print(bool(10))         # Output : True
print(bool(["apple","Strawberry","Mango"])) # Output : True

# Evaluation of Variables
c = "Helloooo there "
d =  0
print(bool(c))          # Output : True
print(bool(d))          # Output : False

"""
False boolean Values
we have
()
[]
""
{}
None
0
False
"""

print( bool(()) )        # Output : False
print(bool([]) )         # Output : False
print(bool(("")) )       # Output : False
print(bool(({}))  )      # Output : False
print(bool((None)) )     # Output : False
print(bool((False)) )    # Output : False

# Another value that returns False is if you have an object of a function with a __len__ function that returns 0 or False

class lenclass():       # defining the class
  def __len__(self):    # defining the function
    return 0

myobject = lenclass()
print(bool(myobject))   # Output : False


""" Functions can also be created such that they return a boolean values """
def myfunction():
    return True
print(myfunction())     # Output : True

# You can execute code based on the boolean value of a function

if myfunction :
    print("Ni ukweli")
else :
    print("Hapana")
# Output : Ni ukweli

# Python has many functions that return boolean values like isinstance
e = 200
print(isinstance(e,int))    # Output : True
