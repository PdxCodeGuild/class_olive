convert = {"km": 1000, "feet": 0.3048,  "mile": 1609.34, "meter": 1, "yard": 0.9144, "inch": 0.0254}
distance = input("What is the distance?: ")
user_units = input("Enter the units, km, feet, mile, meter, yard, inch: ")
unit_2 = input("what are the output units? ")

meters = (float(distance) * convert[user_units])
print(convert[unit_2]/float(meters))