card_value = {"ace": 1, "king": 10, "jack": 10, "queen": 10, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

first_card = input("What's your first card?: ")
second_card = input("What's your second card?: ")
third_card = input("Whats your third card?: ")


total = card_value[first_card] + card_value[second_card] + card_value[third_card]

if total < 17:
    print(total, "Hit")
elif total >= 17 and total < 21:
    print(total, "stay")
elif total == 21:
    print(total, "blackjack!")
else: 
    print("already busted")
















