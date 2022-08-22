import random

def pick_6():
    numbers = []
    for x in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

winning_ticket = pick_6()

count = 0

for x in range(100_000):
    if winning_ticket == pick_6():
        count += 1

balance = -2.0

winnings = {0 : 0, 1 : 4, 2 : 7, 3 : 100, 4 : 50_000, 5 : 1_000_000, 6 : 25_000_000}

if count > 6:
    print("That's crazy.")
else:
    print(f"You won ${balance + winnings[count]}! Your ROI is ${(balance - 2)/2}")