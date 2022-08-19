'''
This program will play pick 6 100,000 thousand times.
'''

import random

#Declare a list variable for our winning numbers and our playing numbers
winning_numbers = []
playing_numbers = []

#Declare a variable for our balance, starting at zero.
balance = 0

#Declare a variable that's a dictionary containing our winning information based on how many matches we get.
winnings_dict = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000

}

#Declare a function for making a list of 6 ints between 0 and 100.
def pick_6_list_generator():
    list_of_6 = []
    for x in range(6):
        list_of_6.append(random.randint(1, 99))
    return list_of_6

#Create our winning list.
winning_numbers = pick_6_list_generator()

#For loop for playing pick6 100,000 times. 
for iteration in range(100000):
    winnings_dict_lookup = 0        #Declare or reset a variable to look up winnings per iteration.
    index_iteration = 0             #Declare or reset a variable for looping through the winnings numbers.
    balance -= 2                    #Subtract 2 from our balance to represent the cost of entry.

    playing_numbers = pick_6_list_generator()       #Overwrite "player_numbers" list with a new set of numbers.
    # print(winning_numbers)
    # print(playing_numbers)
    
    #For loop for comparing "playing_numbers" with "winning_numbers"
    for num in playing_numbers:                         #"num" will become each item in "playing_numbers" one at a time.
        if num == winning_numbers[index_iteration]:     #And if "num" matches the value at the index of 0 with "winning_numbers",
            winnings_dict_lookup += 1                   # add 1 to "winning_dict_lookup".
        index_iteration += 1                            #Add 1 to "index_iteration" so that the next loop with compare sequential indexes of "winning_numbers"
    balance += winnings_dict[winnings_dict_lookup]      #Add to the balance the value that corresponds to the number of matching ints.
    # print(winnings_dict_lookup)

        
print(balance)      #Print the balance.

