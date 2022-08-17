conversions = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km' : 1000, 'yd': 0.9144, 'in': 0.0254}
# ask user to enter distance they would like to convert
#version 1
user_distance = input('what is the distance?')
#converting user input to int
user_distance = int(user_distance)
# ask user for the unit of measure
unit = input('what is the unit of measure?')
converted = conversions[unit] * user_distance 
# user answer to int
print(f'{user_distance} {unit} is {converted}m')

