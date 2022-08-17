'''
This lab converts numbers characters to their english representation.
'''

#Dictionary for the ones place or hundreds
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

#Dictionary for tens place
Convert_tens_place_dict = {
    0: '',
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

#List of outliers for conditional statements
list_of_outliers = [10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]

#Dictionary for outliers
Convert_outliers = {
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
    20:'twenty',
    30:'thity',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninty',
}

#While loop for breaking out when printing and future possible utility
while True:
    User_input = int(input('Please enter a number 0-999.\n>: '))     #Ask user for a number and convert to an "int". No error correction.
    if User_input == 0:     #If user input is 0, just print 0.
        print('zero')
        break
    elif User_input in list_of_outliers:        #If user input is in the list of outliers, just print the outliers
        print(Convert_outliers[User_input])
        break
    elif User_input > 99:       #If user input is between 100 and 999, handle those numbers
        hundreds_digit = User_input//100        #Get the hundreds digit by doing floor division with user input
        subtracted_input = (User_input - hundreds_digit*100)      #Get rid of the 100th place so we can check to see if it's an outlier.
        if subtracted_input in list_of_outliers:
            print(f'{Convert_ones_place_dict[hundreds_digit]} hundred {Convert_outliers[subtracted_input]}')      #If the english words for the remander of "subtracted_input are an outlier, print "'x' hundred 'outlier'""
            break
        tens_digit = subtracted_input//10       #If "subtracted_input" is not an outlier, do floor division it for the 10th place.
        ones_digit = User_input%10              #Then, do module division on the user's input. The result will be the ones place.
        print(f'{Convert_ones_place_dict[hundreds_digit]} hundred {Convert_tens_place_dict[tens_digit]} {Convert_ones_place_dict[ones_digit]}' )        #Print ones places dict ' hundred' tens place dict ' ' ones palce dict
        break
    tens_digit = User_input//10     #If user input is between 0 and 99, floor division the tens place and modulas the ones place
    ones_digit = User_input%10
    print(f'{Convert_tens_place_dict[tens_digit]} {Convert_ones_place_dict[ones_digit]}')       #Print the ones place and the tens place.
    break

       




