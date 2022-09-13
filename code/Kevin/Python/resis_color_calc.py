'''
This program calculates resistors via their color bands
'''

band_1_and_2 = {'black' : '0','brown': '1','red': '2','orange': '3','yellow': '4','green': '5','blue': '6','violet':'7','grey': '8','white': '9'}

band_multiplier = {'black' : 1,'brown': 10,'red': 100,'orange': 1000,'yellow': 10000,'green': 100000,'blue': 1000000,'violet':10000000,'grey': 100000000,'white': 1000000000,'gold': 0.1,'silver': 0.01}

band_tolerance = {'brown': ['+-1%',1.01, 0.99],'red': ['+-2%',1.02, 0.98],'green': ['+-0.5%', 1.005, 0.995],'blue': ['+-0.25%', 1.0025, 0.9975],'violet': ['+-0.1%', 1.001, 0.999],'grey': ['+-0.05%', 1.0005, 0.9995],'gold': ['+-5%', 1.05, 0.95],'silver': ['+-10%', 1.10, 0.90]}

def band_calculator(color_1, color_2, color_3, color_4):
    band_str =''
    band_value = int(band_1_and_2[color_1] + band_1_and_2[color_2])
    print(band_value, type(band_value))
    band_value = band_value * band_multiplier[color_3]
    print(band_value)
    if band_value > 1000000000:
        band_value *= .000000001
        band_str = 'G'
    elif band_value > 1000000:
        band_value *= 0.000001
        band_str = 'M'
    elif band_value > 1000:
        band_value *= 0.001
        band_str = 'k'
    return_f_str = f'''
Your resistor is {round(band_value, 4)}{band_str} Ohms with a tolerance of {band_tolerance[color_4][0]},
which is between {round(band_value * band_tolerance[color_4][2], 4)}{band_str} Ohms and {round(band_value * band_tolerance[color_4][1], 4)}{band_str} Ohms.'''
    return return_f_str


