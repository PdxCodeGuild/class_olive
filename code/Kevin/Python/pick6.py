'''
This program will play pick 6 however many times the user inputs.
'''

import random

#Declare a function for making a list of 6 ints between 0 and 100.
def pick_6_list_generator():
    list_of_6 = []
    for x in range(6):
        list_of_6.append(random.randint(1, 99))
    return list_of_6

#Declare a function for playing pick 6
def play_pick_6(user_int, balance=0):
    #Declare a list variable for our winning numbers and our playing numbers
    winning_numbers = []
    playing_numbers = []

    #Declare a variable for our earnings, starting at zero.
    earnings = 0

    #Declare a variable for our expenses, starting at zero.
    expenses = 0

    #Declare a variable to return lists.
    numbers_over_time = []

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



    #Create our winning list.
    winning_numbers = pick_6_list_generator()

    #For loop for playing pick6 the amount of times the user inputs.
    for x in range(user_int):
        winnings_dict_lookup = 0        #Declare or reset a variable to store winnings per iteration.
        index_iteration = 0             #Declare or reset a variable for looping through the winning numbers.
        expenses += 2


        playing_numbers = pick_6_list_generator()       #Overwrite "player_numbers" list with a new set of numbers.
        numbers_over_time.append(playing_numbers)       #Add playing numbers to a list to return
        # print(winning_numbers)
        # print(playing_numbers)

        #For loop for comparing "playing_numbers" with "winning_numbers"
        for num in playing_numbers:                         #"num" will become each item in "playing_numbers" one at a time.
            if num == winning_numbers[index_iteration]:     #And if "num" matches the value at the index of 0 with "winning_numbers,"
                winnings_dict_lookup += 1                   # add 1 to "winning_dict_lookup."
            index_iteration += 1                            #Add 1 to "index_iteration" so that the next loop will compare sequential indexes of "winning_numbers."
        earnings += winnings_dict[winnings_dict_lookup]
    # print(winnings_dict_lookup)
    balance = (balance - expenses) + earnings
    #Return a dictionary of the results.
    return {
        "balance":balance,
        "expenses":expenses,
        "earnings":earnings,
        "winning numbers":winning_numbers,
        "your numbers":numbers_over_time

    }