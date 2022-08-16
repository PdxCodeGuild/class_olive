# Lab02

# Version 1 Ask the user for the number of feet, and print out the equivalent distance in meters. 
# Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048.

# convert = {
#     'feet': 0.3048,
#     'meters': 1,
# }

# distance = input("How many feet?: ")
# distance = int(distance)
# converted = distance * convert['feet']
# print(f"{distance} ft converted to meters is {converted} m.")

# Version 2 Allow the user to also enter the units. Then depending on the units, convert the distance
# into meters. The units we'll allow are feet, miles, meters, and kilometers.

# convert = {
#     'feet': 0.3048,
#     'miles': 1609.34,
#     'meters': 1,
#     'km': 1000,
# }

# units = input("Which unit are you starting with?  Enter either feet, miles, meters, or km: ")
# distance = input("What is the distance in " + units + "?: ")
# distance = int(distance)
# converted = distance * convert[units]
# print(f"{distance} {units} converted to meters is {converted} m.")

# Version 3 Add support for yards and inches

# convert = {
#     'feet': 0.3048,
#     'miles': 1609.34,
#     'meters': 1,
#     'km': 1000,
#     'yards': 0.9144,
#     'inches': 0.0254,
# }

# units = input("Which unit are you starting with?  Enter either feet, miles, meters, km, yards, or inches: ")
# distance = input("What is the distance in " + units + "?: ")
# distance = int(distance)
# converted = distance * convert[units]
# print(f"{distance} {units} converted to meters is {converted} m.")

# Version 4 Ask for distance, starting units, and units to convert to

convert = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'km': 1000,
    'yards': 0.9144,
    'inches': 0.0254,
}

startunit = input("Which unit are converting from?  Enter either feet, miles, meters, km, yards, or inches: ")
distance = input("What is the distance in " + startunit + "?: ")
endunit = input("Which unit are you converting to? Enter either feet, miles, meters, km, yards, or inches: ")
distance = float(distance)   # changed int from previons version to float to allow for decimals
convert_to_meters = distance * convert[startunit]
convert_from_meters = convert_to_meters / convert[endunit]
convert_from_meters = float(convert_from_meters)
print(f"{distance} {startunit} converted to {endunit} is {convert_from_meters} {endunit}.")