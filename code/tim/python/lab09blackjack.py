## Lab 09 Blackjack Advice

cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

print("Valid cards are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K")
card_one = input("What is your first card?: ").capitalize()
card_two = input("What is your second card?: ").capitalize()
card_three = input("What is your third card?: ").capitalize()

if card_one == "A":
    card_one = int(input("Is card one a 1 or 11?: "))
    # total = int(card_one) + cards[card_two] + cards[card_three]
else:
    card_one = cards[card_one]

if card_two == "A":
    card_two = int(input("Is card two a 1 or 11?: "))
    # total = cards[card_one] + int(card_two) + cards[card_three]
else:
    card_two = cards[card_two]

if card_three == "A":
    card_three = int(input("Is card three a 1 or 11?: "))
    # total = cards[card_one] + cards[card_two] + int(card_three)
else:
    card_three = cards[card_three]
# total = cards[card_one] + cards[card_two] + cards[card_three]

total = card_one + card_two + card_three



if total < 17:
    print(f"Your total is {total}, and you should Hit!")

elif total >= 17 and total < 21:
    print(f"Your total is {total}, and you should Stay.")

elif total == 21:
    print(f"Your total is {total}, that's a Blackjack!")

elif total > 21:
    print(f"Your total is {total}, walk away from the table, you already lost.")

else:
    print("How did you even get to this result?")
