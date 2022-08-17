# Lab 03 Number to Phrase

# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. 
# Handle numbers from 0-99.

# Hint 1: you can use modulus to extract the ones and tens digit.
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

import random

# x = 10    # To test specific numbers
x = random.randint(0,99)
tens_digit = x//10
ones_digit = x%10

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
    print(f"{x} in english is - {weirdos_eng[str(x)].title()}")

elif x >= 10 and x < 20:
    print(f"{x} in english is - {weirdos_eng[str(x)].title()}")

else :
    print(f"{x} in english is - {tens_eng[str(tens_digit)].title()} {ones_eng[str(ones_digit)].title()}")