ones_phrase = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', 
'5': 'five', '6':'six', '7': 'seven','8': 'eight', '9': "nine", '0': '' }

tens_phrase = {'1': 'ten', '2': 'twenty', '3': 'thirty', '4':'forty','5': 'fifty',
'6':'sixty', '7':'seventy', '8': 'eighty', '9': 'ninety', '0': ''}

teens_phrase = {'11': 'eleven', '12': 'twelve', '13': 'thirteen','14': 'fourteen', 
'15': 'fifteen', '16':'sixteen', '17': 'seventeen', '18': 'eighteen', '19':'nineteen', '0': ''}

hundred_phrase = {'1': 'one hundred', '2': 'two hundred', '3': 'three hundred', '4': 'four hundred',
'5':'five hundred', '6': 'six hundred', '7': 'seven hundred', '8':'eight hundred', '9': 'nine hundred', '0': ''}



number = input('enter a number')

if int(number) >= 10:
    if int(number) >10 and int(number) <20:
        
        print(teens_phrase[number])
    elif int(number)< 100: 
        tens_digit = number[0]
        ones_digit = number[1]
        print(tens_phrase[tens_digit]+ ones_phrase[ones_digit])
    else: 
        hundred_digit = number[0]
        ones_digit = number[2]
        tens_digit = number[1]
        if int(tens_digit + ones_digit) > 10 and int(tens_digit + ones_digit) < 20:
            teens_digit = tens_digit + ones_digit 
            teens_digit = teens_phrase[teens_digit]
            print(hundred_phrase[hundred_digit] + teens_digit)
        else:
         print(hundred_phrase[hundred_digit] + tens_phrase[tens_digit]+ ones_phrase[ones_digit])


elif int(number) < 10: 
    ones_digit = number[0]
    print(ones_phrase[ones_digit])

