"""
Fundamentals
"""

# Variables ---------------------------------------------------------------------------------------------------------
# Variables are names given to objects. These allow us to specify the operations we'd like to perform on 
# that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables.
# Everything in Python is an object.

# store data in a name space


from turtle import width


x = 5

# print(x) # 5

# We can easily re-assign a variable in python. Re assign the value of x to 10

x = 10

# print(x) # 10


# Python does not need us to declare the data type of our variables. It is the data type of whatever is stored in it.
# Re assign x to a string without issue

x = 'Hello World'

# print(x) # Hello World

# Manipulating the data already stored in a variable -----------------------------------------------------------------

color = 'red'

# variable 'color' IS a string because it CONTAINS a string
# print(type(color)) # <class 'str'>

color = color.upper()

# print(color) # RED

# Python variable naming conventions -----------------------------------------------------------------

'''
Python Variable Names
- must start with a letter or underscore character
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are three different variables)
'''

age = 18
Age = 19 # dont use casing
AGE = 20 # dont use casing

# print(age) # all three different storage spaces


# python_variable_and_function_names_use_snake_case
# all lowercase words separated with underscores

# ThisIsTitleOrPascalCase - used in Python for defining classes (custom datatypes)


# Basic built in Function --------------------------------------------------------------------------------------------------------

# print('hello') 

# print() prints data in the terminal. Returns None
# It can take multiple comma separated arguments. PLEASE use this to label your data with testing. It helps
# stop confusion.

x = 3.14

# print("Pie:", x) # Pie: 3.14


# input() allows the user to interact with the terminal as it pauses and waits for the users to type in information. Once the user
# hits enter, anything typed into the terminal will be returned in place. We can then store it into a variable

# name = input("Enter a name: ")

# print(name)


# Using the print without variable assignment is generally pointless unless it is purley being used like a welcome message as the data is 
# not stored in your program.


# print("welcome", input('Enter your name: '))

# print(name)  # NameError: name 'name' is not defined


# Datatypes ---------------------------------------------------------------------------------------------------------
# Since everything in Python is an object, we can check the data type of the object, or a variables value by using
# the type()

# Check type() on literals

# print(type(None)) # <class 'NoneType'>
# print(type('hello'))  # <class 'str'>
# print(type(5)) # <class 'int'>
# print(type('5'))  # <class 'str'>
# print(type([])) # <class 'list'>

# Check type() on variables

x = 5 
# print(type(x)) # <class 'int'>


x = '5'
# print(type(x)) # <class 'str'>

x = False
# print(type(x)) # <class 'bool'>


# Typecasting --------------------------------------------------------------------------------------------------------

# In Python, we can easily convert our literals or variables value by using typecasting functions

# Typecast on literals 

x = 5

# print(type(x)) # <class 'int'>

x = str(x) 

# print(x) # 5
# print(type(x)) #  <class 'str'>


y = '5'
y = float(y)

# print(y)


# Concatenation --------------------------------------------------------------------------------------------------------
# Adding strings together to return a combined string

# print('Welcome' + ' Class' + ' Olive')  # Welcome Class Olive

name = 'Bob'

message = 'Hello '

greeting = message + name

# print(greeting) # Hello Bob


# Working with Data returned from input() -------------------------------------------------------------------------------

# the input() always returns a string. This works perfectly with concatenation

# name = input("Enter your name: ")
# print('Welcome ' + name) 



# Since the input() always returns a string, it will not work with operations like normal math

# number = input("Enter a number: ")

# print(number + 5) # TypeError: can only concatenate str (not "int") to str


# In order to treat the value of the number variable as a number, we need to typecast it into a int or float


# number = input("Enter a number: ")

# number = int(number)

# print(number + 5) # 6



# F strings -------------------------------------------------------------------------------
# stands for formatted. F strings make printing easier

city = 'Portland'
temp = 70 # integer - int


# concatenation only works between strings
# other datatypes will need to be "typecast" as strings using str()
# str(object) - return a string representation of the object


message = 'Welcome to ' + city + '! The temp today was ' + str(temp) + ' degrees!'

# print(message) # Welcome to Portland! The temp today was 70 degrees!

'''
f-string
- 'f' stands for 'formatted'
- begin with and 'f' before the opening quote
- Python expressions (code) can be placed within the f-string using curly brackets {}
- don't care about datatype
'''

message = f"Welcome to {city}! the temp today was {temp} degrees!" 

# print(message) # Welcome to Portland! The temp today was 70 degrees!


# Find the area of a rectangle with user-defined sides

# have the user define the height and width of a rectangle
height = input("Enter the height of the rectangle: ")
width = input("Enter the width of the rectangle: ")

# convert the height and width from strings to floats
height = float(height)
width = float(width)

# calculate the area 
area = height * width

result = f'''
Area of a Rectangle
-------------------
height ... {height}
width .... {width}

area ..... {area}
'''
# print(result)