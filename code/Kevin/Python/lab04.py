'''
This program advices wether you should stay or hit in Blackjack (probably don't gamble though).
'''

#Card point value dictionary
CARD_VALUE_DICT = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10
}

input_card_1 = input("What's your first card?\n>: ").upper()
input_card_2 = input("What's your second card?\n>: ").upper()
input_card_3 = input("What's your third card?\n>: ").upper()
result = CARD_VALUE_DICT[input_card_1]+CARD_VALUE_DICT[input_card_2]+CARD_VALUE_DICT[input_card_3]

if result < 17:
    print(f'{result} Hit')
elif result < 21:
    print(f'{result} Stay')
elif result == 21:
    print(f'{result} Blackjack!')
elif result > 21:
    print(f'{result} Already Busted')