

ones_to_text = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    0 : 'Zero'
}
teens_to_text = {
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen',
    10 : 'Ten'
}
tens_to_text = {
    2 : 'Twenty',
    3 : 'Thirty',
    4 : 'Fourty',
    5 : 'Fifty',
    6 : 'Sixty',
    7 : 'Seventy',
    8 : 'Eighty',
    9 : 'Ninety'
}

hundreds_to_text = {
    1 : 'One Hundred and',
    2 : 'Two Hundred and',
    3 : 'Three Hundred and',
    4 : 'Four Hundred and',
    5 : 'Five Hundred and',
    6 : 'Six Hundred and',
    7 : 'Seven Hundred and',
    8 : 'Eight Hundred and',
    9 : 'Nine Hundred and'
}

x = int(input("Hi, put in any number between 0 and 1000 to convert the number into words: "))
hundreds_digit = x//100
tens_digit = x//10%10
ones_digit = x%10
teens_check = x%50

'''
print(hundreds_digit)
print(tens_digit)
print(ones_digit)
print(teens_check)
''' 

if x > 99 and x < 1000:
    if teens_check > 9 and teens_check < 20:
        print(f' {hundreds_to_text[hundreds_digit]} {teens_to_text[teens_check]}')
    elif ones_digit == 0 and tens_digit == 0:
        print(f' {hundreds_to_text[hundreds_digit]} Zero')
    elif ones_digit == 0:
        print(f' {hundreds_to_text[hundreds_digit]} {tens_to_text[tens_digit]}')
    else:
        print(f' {hundreds_to_text[hundreds_digit]} {tens_to_text[tens_digit]}-{ones_to_text[ones_digit]}')
elif x > 19 and ones_digit != 0:
    print(f' {tens_to_text[tens_digit]}-{ones_to_text[ones_digit]}')
elif x > 19 and ones_digit == 0:
    print(f' {tens_to_text[tens_digit]}')
elif x < 20 and x > 9:
    print(f'{teens_to_text[x]}')
elif x < 10 and x >= 0:
    print(ones_to_text[ones_digit])

'''


Version 3 - in progress



roman_numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM'
    }

numerals_desc = list(sorted(roman_numerals.keys(),reverse=True))


print(numerals_desc)



def roman_converter(x):
    
    roman_numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    result = []

    numerals_desc = list(sorted(roman_numerals.keys(),reverse=True))

    for z in numerals_desc:
        if x != 0:
            one_down = x//z

            if one_down != 0:
                for y in range(one_down):
                    result.append(roman_numerals[z])
        x = x%z
    print(''.join(result))


romans = int((input("Let's convert an integer to a Roman Numeral: ")))

while romans > 0:
    roman_converter(romans)
    romans = int(input("Type 0 to end or any number to obtain a new roman numeral: "))

print('Thanks for using the Roman Numeral converter!')
    




Version 4



ones_to_text = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    0 : 'Zero'
}
teens_to_text = {
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen',
    10 : 'Ten'
}
tens_to_text = {
    2 : 'Twenty',
    3 : 'Thirty',
    4 : 'Fourty',
    5 : 'Fifty',
}

hr = int(input('Enter the Hour you want to convert into a word: '))
mins = int(input('Enter the Minutes you want to convert into a word: '))
am_pm = input('Enter am or pm: ').upper()

if mins > 9 and mins < 20:
    print(f'{ones_to_text[hr]} {teens_to_text[mins]} {am_pm}')
elif mins > 19:
    print(f'{ones_to_text[hr]} {tens_to_text[mins//10%10]}-{ones_to_text[mins%10]} {am_pm}')
else:
    print(f"{ones_to_text[hr]} o'{ones_to_text[mins%10]} {am_pm}")
'''