'''
Types of division
'''

import random

# A / in python is regular division. It always results in a float ---------------------------------------------------

x = 5

result = x / 2

# print(result) # 2.5

y = 1

# print(1/1) # 1.0



# A // in python is floor division. It always gives us a whole number rounded down. 
# example. 9.9 would be 9

x = 5

result = x // 2

# print(result) # 2



# A third type of division is modulus or the % 

x = 5

# print(75 % 10) # 5



# ------------------------------------------------------------------------------------------ #

# // and % are compliments 
# print(75 / 10)  # 7.5
# print(75 // 10) # 7
# print(75 % 10)  # 5

number = 187

# print(number % 10)




# Comparison Operators - compare two pieces of data and result in a boolean

x = 5 
y = 5

# = is the assignment operator 

# print(x == y) # True
# print(x != y) # False

# print(x < y)  # < 'strictly' less than - False
# print(x <= 5) # <= less than or equal to - True


# print(x > y) # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True


# check for a particular value in a variable
# print(x == 5)

# print(True == True)
# print(True == False) # False


# ------------------------------------------------------------------------------------------ #
# Conditional statements
# or know as if statements

# an if statement looks for True, and if it is True goes into a code block executing some code

x = 5

# if x == 5:
#     print('we made it into the code block ')


'''

Conditional Statements - if / elif / else
Run different code blocks based on the outcome of comparisons.

Code Block

----------
A section of code that executed together.
In Python, code blocks are defined using horizontal indentation

- must start with if
- every single if statement will be checked
- elif will only be checked if the preceding if and other elifs were False
- if/elif will only be checked until a True condition is found
- else will be run if all other conditions were False
'''




# ----------------------------------------------------------------------- #

light_switch = 'Error'

if light_switch == 'ON':
    message = 'I can see'

elif light_switch == 'OFF':
    message = "It's dark in here"

elif light_switch == 'DIM':
    message = 'The light is dim...'

else:
    message = 'The light is broken'

# print(message)


# -------------------------------------------------------------------------------------- # 


x = 140
y = 140

if x < y:
    output = f"{x} is less than {y}"

elif x == 14:
    output = "x is 14"

elif x > y:
    output = f"{x} is greater than y"    

else:
    output = f"x and y are both {x}"
 
# print(output)

# ---------------------------------------------------------------------------------- #


# secret = 5
secret = random.randint(1, 10)

# print(secret) 

# ask the user to guess a number 
guess = input("Guess a number between 1 and 10: ")

guess = int(guess)


# compare the guess to the secret
if guess == secret:
    print("Congrats they are the same")

elif guess < secret:
    print(f"Oops, you guessed too low. Guess {guess} Secret {secret}")

elif guess > secret:
    print(f"Oops, you guessed too high. Guess {guess} Secret {secret}")