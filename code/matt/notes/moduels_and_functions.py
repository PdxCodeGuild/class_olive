'''
Modules and Functions 
'''

import the_raven

# Importing Modules --------------------------------------------------------------------------------------------------------------------
# the import keyword allows data from outside our file to be brought into the file we are currently working on

text = the_raven.the_raven_text
# print(text)


# Python comes with many built in modules. These are files on your computer that python knows to look for when given their key words.
# here are examples of a few.


import random
import string
import turtle
import math
import email

# note that normally, all imports would be directly on top in your file. This is so the whole contents of our file has
# access to the information


# Random is very useful. By importing it, we have access to many powerful math methods and 
# functions which make it so we don't have to build them ourselves

# Generate a random number between 1 and 100

number = random.randint(1, 100) # randint() takes two arguments, the smallest possible number, the highest and returns a random selection

# print(number)

students = ['kevin', 'tim', 'lauren', 'robert', 'rebeca']

chosen_student = random.choice(students)

fruit = 'apples'

random_char = random.choice(fruit)

# print(random_char)


# Function ---------------------------------------------------------------------------------------------------------------------

# A function is a block of code which only runs when it is called. (called means ()  to run it)
# You can pass data, known as parameters, into a function.
# A function returns data as a result.
# If no data is returned, Python by default returns None


# define a function---------------------------------------------------------------------------------------------------------------------

# This function named add_numbers, takes in two numbers and returns the sum of the two numbers

def add_numbers(number_1, number_2):
    return number_1 + number_2




# Call the function with () after its name to run it and get the returned value
# print(add_numbers(5, 10)) # 15

result = add_numbers(5, 1)
# print(result)

# Parameters and Arguments ---------------------------------------------------------------------------------------------------------------------

# Arguments is the data being provided to the function
# Parameters are clones of that data that ONLY exist inside the function. The are empty vessels until data is given to them


def tell_dogo_what_they_are(name, sex):
    return f'{name} is a good {sex}!'


# print(tell_dogo_what_they_are('Dug', 'boy'))

name = 'Suzzy'
gender = 'girl'

# print(tell_dogo_what_they_are(name, gender))

# Questions: Why wont these works?
# print(tell_dogo_what_they_are()) # We are missing arguments for the 2 parameters 
# print(tell_dogo_what_they_are(name)) # We are missing 1 argument for sex
# print(tell_dogo_what_they_are(gender, name)) # Arugments are out of order



# New Example ---------------------------------------------------------------------------------------------------------------------
"""
def is_user_banned(user_name):
    banned_users = ['Evil_Greg', 'Carl', 'Tammy', 'All_Karens']
    if user_name in banned_users:
        return True
    return False

user = input("Enter the username: ")

banned = is_user_banned(user)

if banned == True:
    print(f"Sorry {user}, you were banned")
else:
    print(f"Welcome {user}")

"""
# Grading Lab WITHOUT Functions ---------------------------------------------------------------------------------------------------------
# Very repetitive

"""
grade = input("enter the score and I will tell you a letter grade: ")
grade = int(grade)

rivial_grade = random.randint(0, 100)

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
elif grade <= 59:
    letter_grade = 'F'

if rivial_grade >= 90:
    letter_grade_rival = 'A'
elif rivial_grade >= 80:
    letter_grade_rival = 'B'
elif rivial_grade >= 70:
    letter_grade_rival = 'C'
elif rivial_grade >= 60:
    letter_grade_rival = 'D'
elif rivial_grade <= 59:
    letter_grade_rival = 'F'



print(f"You score a {grade} and got a {letter_grade}")
print(f"You score a {rivial_grade} and got a {letter_grade_rival}")"""



# Grading Lab WITH Functions:
# reduces the repetitive nature of this code 

"""
def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

user_grade = input("Enter the numeric score you got on your test: ")
user_grade = int(user_grade)
letter_grade = get_letter_grade(user_grade)

rival_grade = random.randint(0, 100)
rival_letter_grade = get_letter_grade(rival_grade)

print(f"\nYou scored a {user_grade} receiving a {letter_grade} and your rival scored a {rival_grade} receiving a {rival_letter_grade}")
"""


# x = 0

# while x < 100000:
#     x += 1
#     print(x)

# print(x)


for x in range(100000):
    print(x)