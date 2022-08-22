from itertools import count
import random

def ticket():
    ticket =[]
    for i in range(6):
        ticket.append(random.randint(0,99))
    return ticket


def pick_6():

    attempts = int(input("How many times would you like to try and win: ")) # attempts to check

    cost = 0

    win_count = []

    win_count = 0

    winnings = 0

    pick_6_w = []

    pick_6_rand = []

    pick_6_w = ticket()
    
    while attempts != 0:

        win_count = 0

        pick_6_rand = ticket()

        for index in range(6):
            if pick_6_rand[index] == pick_6_w[index]:
                win_count += 1

        if win_count == 1:
            winnings += 4
        elif win_count == 2:
            winnings += 7
        elif win_count == 3:
            winnings += 100
        elif win_count == 4:
            winnings += 50000
        elif win_count == 5:
            winnings += 1000000
        elif win_count == 6:
            winnings += 25000000

        cost +=2
        attempts -= 1

    print(pick_6_rand)
    print(pick_6_w)
    print(winnings)
    print(win_count)

    if cost < winnings:
        print(f"Well, you spent ${cost} and won ${winnings}. In total, that's a loss of, wait... holy hell, you broke the odds and earned ${winnings-cost}. Your ROI was {(winnings-cost)/cost}.")
    elif winnings < cost:
        print(f"Well, you spent ${cost} and won ${winnings}. In total, that's a loss of ${abs(winnings-cost)}. The winning numbers were {pick_6_w}. Your ROI was {(winnings-cost)/cost}.")

pick_6()
                


