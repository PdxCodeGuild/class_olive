def is_credit_number_valid(credit_number):
    credit_number = list(credit_number)
    check_digit = credit_number.pop(-1)
    credit_number.reverse()
    sum = 0
    for i in range(len(credit_number)):
        credit_number[i] = int(credit_number[i])
        if i % 2 == 0:
            credit_number[i] *= 2
        if credit_number[i] > 9:
            credit_number[i] -= 9
        sum += credit_number[i]
    sum = str(sum)
    return sum[1] == check_digit

        

credit_number = input("What is your credit card number? ")
if is_credit_number_valid(credit_number):
    print("Valid!")
else:
    print("Authorization failed.")



