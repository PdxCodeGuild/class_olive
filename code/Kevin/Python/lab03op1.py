'''
This lab converts numbers characters into roman numerals.
'''

#Dictionary for the ones place.
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

#While loop for breaking out when printing and future possible utility
while True:
    User_input = int(input('Please enter a number 0-99 to turn roman.\n>: '))       #Ask user for an input and store it as an "int"
    if User_input in range(40, 50):     #If the user's input within this range, concatenate an "XL" to the ones place str.
        ones_place = User_input%10      #Convert ones place to Roman.
        print('XL'+Convert_ones_place_dict[ones_place])     #Print Roman numeral.
        break       #Finish
    elif User_input in range(90,100):        #If the user's input is within this range, concatenate an "XC" to the ones place str.
        ones_place = User_input%10          #Convert ones place to roman
        print('XC'+Convert_ones_place_dict[ones_place])     #Print Roman numeral.
        break
    elif User_input > 49:       #If above 49, do math here instead of line 43.
        tens_place = User_input//10 - 5     #Get the tens place and minus 5 from it. 
        ones_place = User_input%10          #Get ones place.
        tens_place_str = ''                 #Initialize a str variable.
        for x in range(tens_place):     #Concatenate an "X" for however many times is inside "tens_place".
            tens_place_str += 'X'
        print('L'+tens_place_str+Convert_ones_place_dict[ones_place]) 
        break 
    elif User_input//11 == 0:       #If the input is 0 to 10, just print that roman numeral
        print(Convert_ones_place_dict[User_input])
        break
    tens_place = User_input//10     #Get tens place
    ones_place = User_input%10      #Get ones place
    tens_place_str = ''             #Initialize str variable
    for x in range(tens_place):     #Concatenate an "X" for however many times is "tens_place".
        tens_place_str += 'X'
    print(tens_place_str+Convert_ones_place_dict[ones_place])

    
