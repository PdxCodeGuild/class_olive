user_input = input("enr your credit card number : \n")
credit_card_num = [int(x) for x in user_input]
print(credit_card_num)
check_digit = credit_card_num.pop()
print(credit_card_num)
credit_card_num.reverse()
print(credit_card_num)
doubled_list = []

sub_list = []

index = 0
for x in credit_card_num:
    if index % 2 == 0:
        doubled_list.append(x * 2)
    else:
        doubled_list.append(x)
    index += 1
        
print(doubled_list)
for x in doubled_list:
    if x > 9:
        sub_list.append(x - 9)
    else:
        sub_list.append(x)
        
        
print(sub_list)
sum_of_list = sum(sub_list)


print(sum_of_list)
checked_list = sum_of_list % 10
print(checked_list)
if checked_list == check_digit:
    print("valid")



