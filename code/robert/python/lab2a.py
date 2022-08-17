'''
Version 1

user_to_calc = int(input("Howdy! Put in a measurement in feet and we'll our robot will convert it into meters: "))
calc_out = user_to_calc*.3048
print(f'{user_to_calc} ft is {calc_out} m')
'''

'''
Version 2

meter_convert = {
    'ft': 0.3048,  
    'mi': 1609.34,
    'm' : 1,
	'km': 1000
}

user_to_calc = input("Howdy, what's the distance we're trying to measure: ")
units_to_calc = input("And what kind of units are we using (ft,mi,m,km): ")
print(f' {user_to_calc} {units_to_calc} is {meter_convert[units_to_calc]} m')
'''
'''
Version 3

meter_convert = {
    'ft': 0.3048,  
    'mi': 1609.34,
    'm' : 1,
	'km': 1000,
    'yd': 0.9144,
    'in': .0254
}

user_to_calc = input("Howdy, what's the distance we're trying to measure: ")
units_to_calc = input("And what kind of units are we using (ft,mi,m,km,yd,in): ")
print(f' {user_to_calc} {units_to_calc} is {meter_convert[units_to_calc[:2]]} m')
'''

convert_to_meter = {
    'ft': 0.3048,  
    'mi': 1609.34,
    'm' : 1,
	'km': 1000,
    'yd': 0.9144,
    'in': .0254
}

convert_from_meter = {
    'ft': 3.280839895, 
    'mi': 0.0006213727, 
    'm': 1, 
    'km': 0.001, 
    'yard': 1.093613,
    'in': 39.37008
}

input_to_calc = int(input('Howdy, please input the distance: '))
from_unit = input('And what kind of units are we using (ft,mi,m,km,yd,in): ')
to_unit = input('Last question, what are we converting to (ft,mi,m,km,yd,in): ')

print(f'''
{input_to_calc} {from_unit} 
is 
{input_to_calc*convert_to_meter[from_unit]*convert_from_meter[to_unit]} {to_unit}''')
