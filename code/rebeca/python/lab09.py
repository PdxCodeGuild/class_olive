card_value = {'a':1, '2': 2, '3':3 , '4': 4, '5': 5,
'6': 6, '7': 7, '8':8, '9': 9, '10': 10, 'j':10, 'q':10, "k":10 }

first_card = input('what is your first card?')
second_card = input('what is your second card?')
third_card = input('what is your third card?')

total = card_value[first_card] + card_value[second_card] + card_value[third_card]
print(total)

if total < 17:
    print('hit')

if total >= 17 and total < 21:
    print('stay')

if total == 21:
    print('blackjack')

else:
    print('busted')


    
