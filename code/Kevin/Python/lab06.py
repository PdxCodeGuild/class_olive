'''
This lab is for validating a credit card number
'''



def credit_card_validation(cc_num):
    cc_list = []
    cc_list_convert = []

    cc_list += cc_num

    print(cc_list, 'str list')

    for x in cc_list:
        cc_list_convert.append(int(x))

    print(cc_list_convert, 'int convert')

    check_digit = cc_list_convert.pop()

    print(cc_list_convert, "popped off list.","popped digit = ",check_digit)

    for x in range(15):
        if x%2 != 0:
            cc_list_convert[x] *= 2

    print(cc_list_convert, 'double every other')

    for x in range(15):
        if cc_list_convert[x] > 9:
            cc_list_convert[x] -= 9

    print(cc_list_convert, "minus 9 from > 9")

    cc_sum = 0

    for x in cc_list_convert:
        cc_sum += x

    print(cc_sum, "sum all")

    cc_sum %= 10

    print(cc_sum)

    if cc_sum == check_digit:
        return True
    else:
        return False



if credit_card_validation(input("Input a credit card number.\n>: ")) == True:
    print('Valid!')
else:
    print('Invalid')

