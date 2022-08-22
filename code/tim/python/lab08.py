# Lab 08 Pick6
import random

# 1 Generate a list of 6 random numbers representing the winning ticket
# 2 Start your balance at 0
# 3 Loop 100,000 times, for each loop:
#   4 Generate a list of 6 random numbers representing the ticket
#   5 Subtract 2 from your balance (you bought a ticket)
#   6 Find how many numbers match
#   7 Add to your balance the winnings from your matches
# 8 After the loop, print the final balance (Hint: This will be negative)

balance = 0
# matches = 0

def ticket():
    numbers = []
    for x in range(6):
        numbers.append(random.randint(0,99))
    # print(numbers)
    return numbers

def compare_matches(winner, ticket):
    matches = 0
    if winner[0] == ticket[0]:
        matches += 1
    
    if winner[1] == ticket[1]:
        matches += 1

    if winner[2] == ticket[2]:
        matches += 1

    if winner[3] == ticket[3]:
        matches += 1

    if winner[4] == ticket[4]:
        matches += 1    

    if winner[5] == ticket[5]:
        matches += 1

    return matches


winning_ticket = ticket()
# winning_ticket = [16, 59, 49, 83, 3, 4]


print(f"The winning ticket is {winning_ticket}")

winnings = 0
for x in range(100000):
    balance -= 2
    current_ticket = ticket()
    # current_ticket = [16, 59, 49, 83, 3, 4]    # You had 1 matches  -- even when all should be matches
    # print(f"Ticket is {current_ticket}")
    matches = compare_matches(winning_ticket,current_ticket)


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
    
print(f"Your cost is {balance}.")
print(f"You won {winnings}.")
print(winnings + balance)

print(f"Your ROI is {(winnings + balance) / balance}") 