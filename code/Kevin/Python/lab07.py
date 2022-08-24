'''
This program encodes strings into ROT13
'''
import string


#Build a dict for letters for referencing keys.
letter_dict = {
    ' ':0,
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}

#Build a list with letters for referencing the index.
letter_list = [' ','a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Ask the user for a string to decode, then ask their desired ROT.
user_input_str = input('Please enter a string for decoding.\n>: ')
user_input_rot = int(input('Now, enter how much ROT.\n>: '))

#Declare a variable for storing the output string.
output_str = ''

#Loop through the user input, making x each character.
for x in user_input_str:
    letter_value = 0        #Declare and reset a variable for storing the value associated with "x"s character... 
                            # at the appropriate key in "letter_dict."
    if x in string.ascii_letters:        #If "x" is not a letter, go straight to line 66.
        if x in string.ascii_uppercase:     #If x is upper case, lower it for searching through the dict, then uppercase it again before concatenation (line 58).
            letter_value = letter_dict[x.lower()] + user_input_rot      
            while letter_value > 26:        #For as long as "letter_value" is over 26,
                letter_value -= 26          # reduce it by 26.
            output_str += letter_list[letter_value].upper()
        else:
            letter_value = letter_dict[x] + user_input_rot      #If x is not lowercase, then just concatenation normally.
            while letter_value > 26:        #For as long as "letter_value" is over 26,
                letter_value -= 26          # reduce it by 26.
            output_str += letter_list[letter_value]

    else:
       output_str += x

print(output_str)
    