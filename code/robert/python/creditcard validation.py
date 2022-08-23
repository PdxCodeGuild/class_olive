def every_other_is_doubled(numbers):
#Double every other element in the reversed list.
    list = []

    for i,x in enumerate(numbers):
        if i%2 != 0:
            numbers = x
        else:
            numbers = x*2

        list.append(numbers)

    return list

def over_9(numbers):
#Subtract nine from numbers over nine.

    for item in range(0, len(numbers)):
        if numbers[item] > 9:
            numbers[item] = numbers[item] - 9

    return numbers


def number_converter():
#Convert the input string into a list of ints

    credit_card_input = list(input('Enter the Credit Card Numbers: '))

    credit_card_list = [int(i) for i in credit_card_input]

    last_digit_of_card = credit_card_list.pop(15) #Slice off the last digit.  That is the **check digit**.

    #Reverse the digits.

    credit_card_list.reverse()

    doubled_evens = every_other_is_doubled(credit_card_list)
    #Double every other element in the reversed list.

    minus_9 = over_9(doubled_evens)
    #Subtract nine from numbers over nine.

    sum_all = sum(minus_9)
    #Sum all values

    if last_digit_of_card == sum_all%10:
        print('Valid')
    else:
        print("Invalid")

number_converter()