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
    10 : 'One Hundred and',
    20 : 'Two Hundred and',
    30 : 'Three Hundred and',
    40 : 'Four Hundred and',
    50 : 'Five Hundred and',
    60 : 'Six Hundred and',
    70 : 'Seven Hundred and',
    80 : 'Eight Hundred and',
    90 : 'Nine Hundred and'
}

x = 115
hundreds_digit = x%1000
tens_digit = x//10
ones_digit = x%10

print(hundreds_digit)
print(tens_digit)
print(ones_digit)

if x > 19:
    print(f' {tens_to_text[tens_digit]}-{ones_to_text[ones_digit]}')
elif x < 20 and x > 9:
    print(f'{teens_to_text[x]}')
elif x < 10 and x >= 0:
    print(ones_to_text[ones_digit])
elif x > 99 and x < 1000:
    print()