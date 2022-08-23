# Lab 03 Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. 
# Handle numbers from 0-99.
# Hint 1: you can use modulus to extract the ones and tens digit.
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

import random

x = random.randint(0,999)
# x = 701    # To test specific numbers

hundreds_digit = str(x//100)
tens_digit = str(x//10%10)   # Why does the %10 make this work????  
ones_digit = str(x%10)
last_two_digits = tens_digit + ones_digit
# print(type(hundreds_digit))
# print(last_two_digits)
# print(hundreds_digit, tens_digit, ones_digit)  

hundreds_eng = {
    '0': '',
    '1': 'one hundred',
    '2': 'two hundred',
    '3': 'three hundred',
    '4': 'four hundred',
    '5': 'five hundred',
    '6': 'six hundred',
    '7': 'seven hundred',
    '8': 'eight hundred',
    '9': 'nine hundred',
}

tens_eng = {
    '0': '',
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety',
}

ones_eng = {
    '0': '', 
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

weirdos_eng = {
    '0': 'zero',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}

if x == 0 or x == 10:
    print(f"{x} in english is - {weirdos_eng[str(x)].capitalize()}")

elif x >= 10 and x < 20:
    print(f"{x} in english is - {weirdos_eng[str(x)].capitalize()}")
   
elif int(hundreds_digit) >= 1 and int(last_two_digits) == 0:
    print(f"{x} in english is - {hundreds_eng[hundreds_digit].capitalize()}")

elif int(hundreds_digit) >= 1 and int(last_two_digits) >= 10 and int(last_two_digits) < 20:
    print(f"{x} in english is - {hundreds_eng[hundreds_digit].capitalize()} and {weirdos_eng[last_two_digits]}")

elif int(hundreds_digit) >= 1 and int(tens_digit) == 0 and int(ones_digit) >= 1:
    print(f"{x} in english is - {hundreds_eng[hundreds_digit].capitalize()} and {ones_eng[ones_digit]}")

elif int(hundreds_digit) == 0 and int(last_two_digits) >= 0:
    print(f"{x} in english is - {tens_eng[str(tens_digit)].capitalize()} {ones_eng[str(ones_digit)]}") 

else :
    print(f"{x} in english is - {hundreds_eng[str(hundreds_digit)].capitalize()} and {tens_eng[str(tens_digit)]} {ones_eng[str(ones_digit)]}")

## It works!  I may have overcomplicated it with the str/int typecasting and can probably clean that up by just making last_two_digits a string
## then using int() if needed later