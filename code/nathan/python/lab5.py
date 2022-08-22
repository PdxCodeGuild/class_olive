import random

def pick_6():
    numbers = []
    for x in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

def test_ticket(winning, hopeful):
    winnings = {0 : 0, 1 : 4, 2 : 7, 3 : 100, 4 : 50_000, 5 : 1_000_000, 6 : 25_000_000}
    wins = 0
    counter = 0
    while counter < len(winning):
        if winning[counter] == hopeful[counter]:
            wins += 1
        counter += 1
    return winnings[wins] - 2
    
        

winning_ticket = pick_6()

total_winnings = 0
expenses = 0

for x in range(100_000):
    total_winnings += test_ticket(winning_ticket, pick_6())
    expenses += 2

if total_winnings > 0:
    print(f" You won {total_winnings} dollars! Your ROI is {(total_winnings - expenses) / expenses}")
else:
    print(f"Sorry, you didn't win. You ended with {total_winnings} dollars Your ROI is {(total_winnings - expenses) / expenses}")
