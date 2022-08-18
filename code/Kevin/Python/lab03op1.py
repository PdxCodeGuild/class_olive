'''
This lab converts numbers characters to their english representation.
'''

#Dictionary for the ones place or hundreds
Convert_ones_place_dict = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X'
}

#Dictionary for tens place
Convert_fifty_place_dict = {
    4: 'XL',
    5: 'L',
    3: '',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

#List of outliers for conditional statements
list_of_outliers = []

#Dictionary for outliers
Convert_outliers = {}

#While loop for breaking out when printing and future possible utility
while True:
    User_input = int(input('Please enter a number 0-89 to turn roman.\n>: '))
    if User_input in range(40, 49):
        ones_place = User_input%10
        print('XL'+Convert_ones_place_dict[ones_place])
        break
    elif User_input > 49:
        tens_place = User_input//10 - 5
        ones_place = User_input%10
        tens_place_str = ''
        for x in range(tens_place):
            tens_place_str += 'X'
        print('L'+tens_place_str+Convert_ones_place_dict[ones_place]) 
        break 

    elif User_input//11 == 0:
        print(Convert_ones_place_dict[User_input])
        break
    tens_place = User_input//10
    ones_place = User_input%10
    tens_place_str = ''
    for x in range(tens_place):
        tens_place_str += 'X'
    print(tens_place_str+Convert_ones_place_dict[ones_place])

    
