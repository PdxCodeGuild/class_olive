import random


def ticket():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(0, 99))
    return numbers
      
cost = 0
winning_ticket = ticket()
print(winning_ticket)
winnings = 0

for x in range(100000):
    matches = 0
    cost -= 2
    current_ticket = ticket()
    winning_ticket = ticket()
    if current_ticket[0] == winning_ticket[0]:
        matches += 1
    elif current_ticket[1] == winning_ticket[1]:
        matches += 1
    elif current_ticket[2] == winning_ticket[2]:
        matches += 1
    elif current_ticket[3] == winning_ticket[3]:
        matches += 1
    elif current_ticket[4] == winning_ticket[4]:
        matches += 1
    elif current_ticket[5] == winning_ticket[5]:
        matches += 1


    if matches == 1:
            winnings += 4
    elif matches == 2:
            winnings += 7
    elif matches == 3:
            winnings += 100
    elif matches == 4:
            winnings += 50000
    elif matches == 5:
            winnings += 1000000
    elif matches == 6:
            winnings += 25000000
print(winnings + cost)
print(matches)
print(cost)
print(winnings)
print(winnings / cost)