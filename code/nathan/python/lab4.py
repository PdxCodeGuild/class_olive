cards = { 
    'A' : 1,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
    }

card1 = cards[input("What's your first card?")]
card2 = cards[input("What's your second card?")]
card3 = cards[input("What's your third card?")]

sum = card1 + card2 + card3

if sum < 17:
    print(sum, "Hit!")
elif sum >= 17 and sum < 21:
    print(sum, "Stay")
elif sum == 21:
    print(sum, "Blackjack!")
else:
    print(sum, "Already busted")

