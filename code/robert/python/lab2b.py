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


x = 25
tens_digit = x//10
ones_digit = x%10

print(tens_digit)
print(ones_digit)

if x > 19:
   print(f' {tens_to_text[tens_digit]} - {ones_to_text[ones_digit]}')
