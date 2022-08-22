from itertools import count
import random

def pick_6():

    attempts = int(input("How many times would you like to try and win: ")) # attempts to check

    cost = 0

    result = []

    win_count = 0

    winnings = 0

    pick_6_w = []

    pick_6_rand = []

    while len(pick_6_w) < 7:
        pick_6_w.append(random.randrange(1,99))

    while attempts != 0:

        pick_6_rand.clear()
        for i in range(6):
            pick_6_rand.append(random.randrange(1,99))

        for i in pick_6_w:
            result = pick_6_rand.count(i)

        if result > 0:
            win_count += 1
            if result == 1:
                winnings += 4
            elif result == 2:
                winnings += 7
            elif result == 3:
                winnings += 100
            elif result == 4:
                winnings += 50000
            elif result == 5:
                winnings += 1000000
            elif result == 6:
                winnings += 25000000

        cost +=2
        attempts -= 1

    if cost < winnings:
        print(f"Well, you spent ${cost} and won ${winnings}. In total, that's a loss of, wait... holy hell, you broke the odds and earned ${winnings-cost} with {win_count} total wins. The winning numbers were {pick_6_w}. Your ROI was {(winnings-cost)/cost}.")
    elif winnings < cost:
        print(f"Well, you spent ${cost} and won ${winnings}. In total, that's a loss of ${abs(winnings-cost)} with {win_count} total wins. The winning numbers were {pick_6_w}. Your ROI was {(winnings-cost)/cost}.")

pick_6()