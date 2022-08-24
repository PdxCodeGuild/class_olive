#convert input string into int
from tokenize import Double


credit_card_list = []
credit_card = input('enter your credit card number')
#print(credit_card)

for char in credit_card:
    char = int(char)
    credit_card_list.append(char)
    
#print(credit_card_list)

check_digit = credit_card_list.pop()
#print(check_digit)

#reverse the list
credit_card_list.reverse()
#print(credit_card_list)

#double every other element in reverse list

for count , value in enumerate(credit_card_list):
    #print(count)
    #print(value)

    if count % 2 == 0:
        value = value * 2 
        credit_card_list[count] = value 
print(credit_card_list)
# subtract numbers over nine 
for count , value in enumerate(credit_card_list):
    if value > 9:
        credit_card_list[count] = value - 9 
print(credit_card_list)  

# sum all values 
credit_card_list = sum(credit_card_list)
print(credit_card_list)

print('valid!')

