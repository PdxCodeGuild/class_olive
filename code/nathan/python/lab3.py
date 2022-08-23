num_ones = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}

num_teens = {
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen'
}

num_tens = {
    '1' : 'ten',
    '2' : 'twenty',
    '3' : 'thirty',
    '4' : 'fourty',
    '5' : 'fifty',
    '6' : 'sixty',
    '7' : 'seventy',
    '8' : 'eighty',
    '9' : 'ninety'
}


number = input("Please provide a number: ")

if int(number) < 10:
    result_string = num_ones[number]
elif int(number) > 10 and int(number) < 20:
    result_string = num_teens[number]
elif int(number) < 100:
    result_string = num_tens[number[-2]]
    if number[-1] != '0':
        result_string += f"-{num_ones[number[-1]]}"
else:
    result_string = f"{num_ones[number[-3]]}-hundred "
    if number[-2] == '1' and number[-1] != '0':
        result_string += f"{num_teens[number[-2] + number[-1]]}"
    elif number[-2] != '0':
        if number[-1] != '0':
            result_string += f"{num_tens[number[-2]]}-"
        else:
            result_string += f"{num_tens[number[-2]]}"
    if number[-1] != '0' and (number[-2] != '1' and number[-1] != '0'):
        result_string += f"{num_ones[number[-1]]}"
        
print(result_string)

