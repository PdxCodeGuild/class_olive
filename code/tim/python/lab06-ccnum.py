# Lab 6: Credit Card Validation
## Convert the input string into a list of ints
## Slice off the last digit. That is the check digit.
## Reverse the digits.
## Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

cc_string = '4815162342481516'

cc_list = [int(digit) for digit in cc_string]  # I can't believe this worked  [4, 8, 1, 5, 1, 6, 2, 3, 4, 2, 4, 8, 1, 5, 1, 6]

print(f"Original card number -       {cc_list}")  # [4, 8, 1, 5, 1, 6, 2, 3, 4, 2, 4, 8, 1, 5, 1, 6]
check_digit = cc_list.pop(-1)
print(f"Minus the check digit -      {cc_list}")  # [4, 8, 1, 5, 1, 6, 2, 3, 4, 2, 4, 8, 1, 5, 1]
# print(f"Check digit - {check_digit}") # 6

cc_list.reverse() # [1, 5, 1, 8, 4, 2, 4, 3, 2, 6, 1, 5, 1, 8, 4]
print(f"Reversed card number -       {cc_list}")

def multiply(list):
    mult_list = cc_list
    for i in range(len(mult_list)):
        if i % 2 == 0:
            mult_list[i] = mult_list[i]*2
    return mult_list

print(f"Every other number doubled - {multiply(cc_list)}")
