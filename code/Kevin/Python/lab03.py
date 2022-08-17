'''
This lab converts numbers characters to their english representation.
'''

# user_input = input('''Please input a number between 1 and 10 to convert to english.
# >: ''')

# x = 67
# tens_digit = x//10
# ones_digit = x%10

# print(tens_digit, ones_digit)

Convert_ones_place_dict = {
    0: 'zero',
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

Convert_tens_place_dict = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

list_of_outliers = [11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]

Convert_outliers = {
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thity',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninty',
}


while True:
    User_input = int(input('Please enter a number 0-99.\n>: '))
    if User_input in list_of_outliers:
        print(Convert_outliers[User_input])
        break
    tens_digit = User_input//10
    ones_digit = User_input%10

    if tens_digit != 0:
        print(f'{Convert_tens_place_dict[tens_digit]}-{Convert_ones_place_dict[ones_digit]}')
    else:
        print(Convert_ones_place_dict[ones_digit])



