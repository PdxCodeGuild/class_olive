'''
This program is for converting units of measurement to other units of measurements.
'''

import time # Used to make delays for easier terimal reading

#Dictionart for storeing meter mulipliers.
distance_dictionary = {
    'meters': 1,
    'feet': 0.3048,
    'miles': 1609.34,
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254
}

# Following multie line strings used to prompt the user for a unit of measurement, then a number.

prompt_1 = f'''
Let's convert a unit of measurement into another unit of measurement!

Please input a unit of measurement.
Choices include:
* Meters
* Feet
* Miles
* Kilometers
* Yards
* Inches
>: '''

prompt_2 = f'''
Please enter a value for that unit.
>: '''

prompt_3 = f'''
What unit of measurement would you like to convert to?
Choices include:
* Meters
* Feet
* Miles
* Kilometers
* Yards
* Inches
>: '''

#Ask the user for a unit of measurement and store it.
#Place in a while loop for error corection. User must input a key in the 
while True:
    user_input_1 = input(prompt_1).lower()
    if user_input_1 in distance_dictionary:
        break
    else:
        print("You did not type an appropriate response. Please try again.")
        time.sleep(2)



#Ask the user for a number and then convert to a float. 
#Placed in a while loop for error correction in case the user inputs something that cannot be converted.
while True:                                                    
    user_input_2 = input(prompt_2)
    try:
        user_input_2 = float(user_input_2)
        break
        
    except:
        print('Your input was not a number. Please try again.')
        time.sleep(2)

while True:
    user_input_3 = input(prompt_3)
    if user_input_3 in distance_dictionary:
        break
    else:
        print("You did not type an appropriate response. Please try again.")
        time.sleep(2)

#Multiplies the user input by the value stored in the correct key.
math_time = user_input_2 * distance_dictionary[user_input_1]
math_time = math_time * distance_dictionary[user_input_3]

#Print result.
print(f'{user_input_2} {user_input_1.title()} is {math_time} {user_input_3.title()}.')


