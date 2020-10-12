'''
String literals in python are surrounded by either single or double quotation marks
'''

#The strings can be displayed using the print() function
print('Hello')  # output : Hello
print("Hello")  # output : Hello

#Assigning a string to a variable
a = "Hello there"
print(a)        # output : Hello there

#Multiline Strings can be assigned to a variable using tripple quotations
b = """ Hey there hows your day coming up
        My day is looking good so far,thanks """
print(b)        #output : Hey there hows your day coming up
                #         My day is looking good so far,thanks

'''
>>>>>>>>>>>>>>>>>>>>>>>> Strings are arrays in python <<<<<<<<<<<<<<<<<<<<<<<<
Like many other programming languages python strings are arrays of bytes representing unicode characters

python doesn't have the type char , therefore they are represented as strings of length 1
'''
c = "Hey they Stratizen"
print(c[1])     # output : e     -> the first character has an index 0
                #it increments from there therefore the second character which is e has an index of 1


'''
>>>>>>>>>>>>>>>>>>>>>>>> Slicing <<<<<<<<<<<<<<<<<<<<<<<<
you can get a range of characters in a string through slicing by specifying
the index of the start character and the end character separated by a semi colon
'''

d = "Hello buddy"
print(d[0:5])   # output : Hello   - this gives you the range from 0 to 5 inclusive of index 0 and 5


'''
>>>>>>>>>>>>>>>>>>>>>>>> String length using the len() function <<<<<<<<<<<<<<<<<<<<<<<<
you can get a range of characters in a string through slicing by specifying
the index of the start character and the end character separated by a semi colon
'''
print(len(d))   # output : 11


'''
>>>>>>>>>>>>>>>>>>>>>>>> String methods <<<<<<<<<<<<<<<<<<<<<<<<
Python has a set of string methods that you can use to manipulate strings
'''

'''The strip() function removes whitespaces at the beginning and at the end'''
e = " where are we having lunch today "
print(e.strip()) # output : where are we having lunch today


'''The lower() function returns a string in lower case '''
f = "GOOD DAY MY FRIEND"
print(f.lower()) # output : good day my friend


'''The upper() function returns a string in upper case '''
g = "hoot at corners"
print(g.upper()) # output : HOOT AT CORNERS


'''The replace() function replaces a string with another string'''
h = "hooting is bad"
print(h.replace("h","l")) # output : looting is bad


'''The split() function splits strings into substrings where it finds instances of the separator'''
i = "John , Paul , Fred , Mary"
print(i.split(",")) # output : ['John ', ' Paul ', ' Fred ', ' Mary']


"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Check String<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
To check a certain sring or phrase present in a string we use the phrase --'in'-- or --'not in'--
"""
txt = "This is the first isle"
j = "is" in txt
print(j)            # output : True

l = "is" not in txt
print(l)            # output : False


"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> String Concatenation <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
To concatenate two strings we use the + operator
"""

m = "Hello"
n = "Tiri"
o = m + n
print(o)            # output : HelloTiri
print(m+" "+n)      # output : Hello Tiri

'''
We can combine string and numbers using the format() method
The format method takes the argument formats them an places them where the placeholder calibraces are {}
'''
p = "My name is Tiri, i am {} years old"
age = 22

print(p.format(age)) # output : My name is Tiri, i am 22 years old

'''
The format() method takes unlimited number of arguments and places them into their respective placeholders
'''

quantity = 8
itemno = 234
price = 2000

statement = "The number of lether bags is {} , the item number is {} and each costs {}"
print(statement.format(quantity,itemno,price)) # output : The number of lether bags is 8 , the item number is 234 and each costs 2000


''' you can use index numbers to ensure the arguments are placed in the correct place '''
statement2 = "i want to pay {2} per bag and buy {0} pieces with the code {1}"
print(statement2.format(quantity,itemno,price)) # i want to pay 2000 per bag and buy 8 pieces with the code 234

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Escape character <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
To insert characters that are illegal in a string we use escape characters
\ followed by the character you want to insert
"""

myillegalone = "My parents and i went to the so called \"five star\" hotels "
print(myillegalone)     # output :My parents and i went to the so called "five star" hotels

"""
below is the link to more python escape characters and string methods
https://www.w3schools.com/python/python_strings.asp
"""
