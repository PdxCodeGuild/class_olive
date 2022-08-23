conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

distance = input("What is the distance? ")
input_unit = input("What are the input units? ")
output_unit = input("What are the output units? ")

result = round(float(distance) * conversion[input_unit] / conversion[output_unit], 7)
print(f"{distance} {input_unit} is {result} {output_unit}")
