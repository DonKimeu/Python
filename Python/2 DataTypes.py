"""
Python Data types

Text - str
Numeric - int , float , complex
Sequence - list , tuple , range
Mapping - dict
Set types - set , frozenset
Boolean - bool
Binary types - bytes , bytearray , memoryview

"""
#you can get the datatype of any object using the type() function

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#Integer
x = 5
"""
Can also be defined as
x = int(5)
"""
print(type(x))
#output : <class 'int'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""


#String
a = str("hello ")
"""
another way to define it as a string would be
a = "hello"
"""
print(type(a))
#output : <class 'str'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

# float

b = float(20.5)

"""
Could also be defined as
b = 20.5
"""
print(type(b))
#output:<class 'float'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#Complex

c = complex(1j)
"""
Can also be defines as
c = 1j
"""

print(type(c))
#output : <class 'complex'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#list
d = list(("Michelle","Marcus","Cookie","Strawberry"))
"""
Can also be defines as
d = ["Michelle","Marcus","Cookie","Strawberry"]
"""

print(type(d))
#output : <class 'list'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#tuple
e = tuple(("Michelle","Marcus","Cookie","Strawberry"))
"""
Can also be defines as
e = ("Michelle","Marcus","Cookie","Strawberry")
"""

print(type(e))
#output : <class 'tuple'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#range
f = range(6)
print(type(f))
#output : <class 'range'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#dict
g = dict (name = "John", age = 23)

"""
Can also be defined as
g = {"name" : "John", "age" : 23}
"""
print(type(g))
#output : <class 'dict'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#Set

h = set(("apple","banana","orange"))
"""
Can also be defined as
h = {"apple","banana","orange"}
"""

print(type(h))
#output : <class 'set'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#frozenset
i = frozenset(("apple","banana","orange"))
"""
Can also be defined as
i = ({"apple","banana","orange"})
"""

print(type(i))
#output : <class 'frozenset'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#bool
j = bool(5)
"""
Can also be defined as
j = true
"""

print(type(j))
#output : <class 'bool'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#bytes
k = bytes(5)
j = b"Hello"

print(type(k))
#output : <class 'bytes'>
print(type(j))
#output : <class 'bytes'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#bytearray

l = bytearray(5)
print(type(l))
#output : <class 'bytearray'>

"""------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-------"""

#memoryview

m = memoryview(bytes(5))
print(type(m))

#output : <class 'memoryview'>
