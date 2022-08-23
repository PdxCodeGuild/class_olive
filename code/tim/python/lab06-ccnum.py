# Lab 6: Credit Card Validation
## Convert the input string into a list of ints
## Slice off the last digit. That is the check digit.
## Reverse the digits.
## Double every other element in the reversed list.
## Subtract nine from numbers over nine.
## Sum all values.
## Take the second digit of that sum.
## If that matches the check digit, the whole card number is valid.


# cc_string = '4815162342481599'
cc_string = input("Enter a 16 digit number: ")

cc_list = [int(digit) for digit in cc_string]       # I can't believe this worked
print(f"Original card number -       {cc_list}")  

check_digit = cc_list.pop(-1)
print(f"Minus the check digit -      {cc_list}")    # [4, 8, 1, 5, 1, 6, 2, 3, 4, 2, 4, 8, 1, 5, 9]

cc_list.reverse() 
print(f"Reversed card number -       {cc_list}")    # [9, 5, 1, 8, 4, 2, 4, 3, 2, 6, 1, 5, 1, 8, 4]

for index in range(len(cc_list)):
    if index % 2 == 0:
        cc_list[index] = cc_list[index]*2
    if cc_list[index] >= 9:
        cc_list[index] = cc_list[index] - 9

card_sum = str(sum(cc_list))
last_digit = int(card_sum[-1])
print(f"The last digit is {last_digit}, and your check digit is {check_digit}")

if last_digit == check_digit:
    print("This card is valid!")
else:
    print("This card number is not valid.")