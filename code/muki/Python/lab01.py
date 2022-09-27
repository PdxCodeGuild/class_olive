# Lab 01, Will "Muki" Shelnutt

# Version 1 
    # using given list for nums = [5, ,0, 8, 3, 4, 1, 6]
    # thoughts are to run some loops and print sum functions with some math going on
    # i will try to define a function that will do this stuff and use that for version 2

from importlib.abc import MetaPathFinder
from string import ascii_letters

'''
numbahs = [5, 0, 8, 3, 4, 1, 6]
print(numbahs)
print('\n') # trying to make this a little easier to identify when printed

for numbah in numbahs:
    print(numbah)
print('\n') # trying to make this a little easier to identify  when printed

for i in range(len(numbahs)):
    print(numbahs[i])
print('\n') # trying to make this a little easier to identify when printed
print(sum(numbahs)/len(numbahs))
'''
'''
def mean_from_input(total, pieces,): 
    total = sum(total)
    pieces = len(total)
    meanie = total / pieces 
    return meanie
'''
'''
# Version 2
days = input('How many are there?\t')
days = int(days)
months = input('How many groups should there be?\t')
months = int(months)
print(f'The average number of days in a month is: {mean_from_input(days, months)}')
'''
'''numbaahs = []
while True:
    n_entry = input("Please enter a number:\t")
    numbaahs.append(n_entry)
print(numbaahs)
'''

digits = []
while True:
    new_dig = input('please enter an integer or type "q" to quit:\t')
    if new_dig == 'q':
        break
    new_dig = int(new_dig)
    digits.append(new_dig)
av = sum((digits))/len(digits)
print(f'So, the values that you entered were calculated to have an average of: {av}')




