# Lab 7: Credit Card Validation

'''
Let's write a function `credit_card_validator` which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list (starting with the first number in the list).
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.

Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. `True` Valid!
'''
testcard = "4556737586899855"
# testcard = input("Please enter a 16 digit credit card number to validate:\t")   ---- Just in case we wanta use input.
test_card = []
for i in testcard:
    test_card.append(int(i))

# print(testcard)
# print(test_card)
# test_card = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
card_as_list = test_card
# def validate_card(card_as_list):
check_digit = card_as_list.pop(-1)
# print(check_digit)
# print(card_as_list)
card_as_list.reverse()
# print(card_as_list)

# for num in card_as_list:
#     print(num, '-this is the index')
    
for i in range(0,len(card_as_list),2):
    print(i, card_as_list[i])
    card_as_list[i] = card_as_list[i] * 2
# print(card_as_list)

# card_as_list[0] = card_as_list[0] * 2
# card_as_list[2] = card_as_list[2] * 2
# card_as_list[4] = card_as_list[4] * 2
# card_as_list[6] = card_as_list[6] * 2
# card_as_list[8] = card_as_list[8] * 2
# card_as_list[10] = card_as_list[10] * 2
# card_as_list[12] = card_as_list[12] * 2
# card_as_list[14] = card_as_list[14] * 2
# print(card_as_list)

for i in range(0,len(card_as_list)):
    # print(i, card_as_list[i])
    if card_as_list[i] > 9:
        card_as_list[i] = card_as_list[i] - 9
    
    
# if card_as_list[0] > 9:
#     card_as_list[0] = card_as_list[0] - 9
# if card_as_list[2] > 9:
#     card_as_list[2] = card_as_list[2] - 9
# if card_as_list[4] > 9:
#     card_as_list[4] = card_as_list[4] - 9
# if card_as_list[6] > 9:
#     card_as_list[6] = card_as_list[6] - 9
# if card_as_list[8] > 9:
#     card_as_list[8] = card_as_list[8] - 9
# if card_as_list[10] > 9:
#     card_as_list[10] = card_as_list[10] - 9
# if card_as_list[12] > 9:
#     card_as_list[12] = card_as_list[12] - 9
# if card_as_list[14] > 9:
#     card_as_list[14] = card_as_list[14] - 9
print(card_as_list)
card_sum = sum(card_as_list)
if card_sum >= 10:
    rem = card_sum // 10
    remo = card_sum - rem *10
    if remo == check_digit:
        print('Valid!')
    else:
        print('Invalid')
else:
    exit

 

