import random 

#generate a list of 6 random numbers
winning_ticket = [22,27,19,21,56,30]



#ask user to choose 6 numbers
#user_numbers = input('choose six numbers') 


def ticket():
    user_numbers = []
   
    for numbers in range (0,6):
        
        user_numbers.append(random.randint(1,99))
   
    return user_numbers 

#winning_ticket = ticket()
#print(winning_ticket)

cost = 0
winnings = 0

for x in range(100000):
    matches = 0
    current_ticket = ticket()

    cost = cost - 2  
    #print(f'balance is {balance}')
    #print(current_ticket[0])
    #print(winning_ticket[0])

    if current_ticket[0] == winning_ticket[0]:
       matches = matches + 1    
    if current_ticket[1] == winning_ticket[1]:
        matches= matches + 1
    if current_ticket[2] == winning_ticket[2]:
        matches = matches + 1
    if current_ticket[3] == winning_ticket[3]:
        matches = matches + 1
    if current_ticket[4] == winning_ticket[4]:
        matches = matches + 1
    if current_ticket[5] == winning_ticket[5]:
        matches = matches + 1 
    
    if matches == 1:
        winnings = winnings + 4 
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
print(winnings)
print(cost)
print(winnings + cost)

roi = (winnings + cost ) / cost 
print(roi)
    


