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

total = cards[card_one] + cards[card_two] + cards[card_three]
#print(f"Your total is {total}")

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