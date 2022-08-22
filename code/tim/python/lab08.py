# Lab 08 Pick6
from asyncio import current_task
import random

# 1 Generate a list of 6 random numbers representing the winning ticket
# 2 Start your balance at 0
# 3 Loop 100,000 times, for each loop:
#   4 Generate a list of 6 random numbers representing the ticket
#   5 Subtract 2 from your balance (you bought a ticket)
#   6 Find how many numbers match
#   7 Add to your balance the winnings from your matches
# 8 After the loop, print the final balance (Hint: This will be negative)

# def pick6():
#     winner = []
#     balance = 0   
#         for index in range(6):     
#         winner.append(random.randint(1,99))
      
#     print(f"The winning ticket is {winner}")
      
#     for index in range(10):
#         ticket = []
#         balance -= 2
#         # print(f"Your balance is {balance}")       # Works - Your balance is -2   Your balance is -4 ....
#         for index in range(6):
#             ticket.append(random.randint(1,99))
#     # return winner    

# def num_matches(winner, ticket):
#     if winner[0] != ticket[0]:
#         print('no match on 0')

# pick6()    

################################

balance = 0


def ticket():
    numbers = []
    for x in range(6):
        numbers.append(random.randint(0,99))
    return numbers                                      # Why does this display None every loop????  If this is where it's coming from

def compare_matches(winner, ticket):
    if winner[0] != ticket[0]:
        print(f"Winning ticket had {winner[0]} and you had {ticket[0]}.")    # Just making sure this works, will build out

winning_ticket = ticket()
print(f"The winning ticket is {winning_ticket}")

for x in range(3):
    balance -= 2
    current_ticket = ticket()
    # print(f"Ticket is {current_ticket}")
    print(compare_matches(winning_ticket, current_ticket))    



# print(f"Your balance is {balance}.")
# print(compare_matches(winning_ticket, current_ticket))    