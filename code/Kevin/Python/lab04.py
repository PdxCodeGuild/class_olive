'''
This program advices whether you should stay or hit in Blackjack (probably don't gamble though).
'''

#Card point value dictionary
CARD_VALUE_DICT = {
    'A':11,
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


result = 0      #Initialize a variable to store our result in.

input_1 = input("What's your first card?\n>: ").upper()     #Ask the user what their 3 cards are and store them in their own variable.
input_2 = input("What's your second card?\n>: ").upper()
input_3 = input("What's your third card?\n>: ").upper()

input_list = [input_1, input_2, input_3]        #Make a list with each input as an index.

#Loop through the list, adding to "result" the value associated with the corresponding key in the "card_value_dict".
for x in input_list:
    result += CARD_VALUE_DICT[x]

#Ask users, for ever Ace that they have, what they would like the value of that Ace to be.
for x in input_list:
    if x == 'A':
        input_1_or_11 = input('Do you want you ace to be a 1 or an 11?')
        if input_1_or_11 == '1':
            result -= 10


#Print a message if the user should hit or stay, or whether they've already lost or won.
if result < 17:
    print(f'{result} Hit')
elif result < 21:
    print(f'{result} Stay')
elif result == 21:
    print(f'{result} Blackjack!')
elif result > 21:
    print(f'{result} Already Busted')