'''
This lab converts numbers characters to their english representation.
'''

#Dictionary for the ones place and hundreds.
Convert_ones_place_dict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

#Dictionary for tens place and outliers
Convert_tens_place_dict = {
    0: '',
    1: '',
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
}

#List of outliers for conditional statements
list_of_outliers = [10,11,12,13,14,15,16,17,18,19,]

#Declare a variable with an empty string if ' hundred and ' is needed.
and_str = ''

User_input = int(input('Please enter a number 0-999.\n>: '))        #Ask user for a number and convert to an "int". No error correction.
hundreds_digit = User_input//100          #Store 100th place
tens_digit = (User_input%100)//10         #Store 10s place.
ones_digit = User_input%10                #Store ones place
outlier_digit = User_input%100            #Grab the tens and ones place into a single int to check if it's 10-19.
if User_input == 0:     #If user input is 0, print zero.
    print('zero')
elif outlier_digit in list_of_outliers:     #If variable outlier_digit is in the list of outliers, 
    tens_digit = outlier_digit              # make the tens digit that outlier digit.
    ones_digit = 0                          #Ones_digit becomes 0 so it will be an empty str.
elif User_input > 99:
    and_str = ' hundred and '               #If the user input is > 99, change the empty and_str variable in the following print statement to ' hundred and '.
print(f'{Convert_ones_place_dict[hundreds_digit]}{and_str}{Convert_tens_place_dict[tens_digit]} {Convert_ones_place_dict[ones_digit]}') 
       




