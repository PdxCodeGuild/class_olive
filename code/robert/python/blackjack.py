def blackjack(again):

    again = '1'

    blackjack_vals = {
    'a' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'A' : 11
}

    while again != '0':

        first_card = input("What's your first card(a = 1, A = 11): ")
        second_card = input("What's your second card(a = 1, A = 11)?: ")

        value = blackjack_vals[first_card] + blackjack_vals[second_card]
        print(f" Alright, so we're at {value},  let's check the system....")

        if value < 17:
            print('Hit')
            third_card = input("What's your third card(a = 1, A = 11)?: ")
            value2 = value + blackjack_vals[third_card]
            
            if value2 < 17:
                print('Hit')
                fourth_card = input("What's your fourth card(a = 1, A = 11) - btw, do you know how hard it is to get 4 cards under 17?: ")
                value3 = value2 + blackjack_vals[fourth_card]
                
                if value3 < 21:
                    print('Stay')
                elif value3 == 21:
                    print('Winner Winner Chicken Dinner')
                else:
                    print('Ooof, unlucky')

            elif value2 < 21:
                print('Stay')
            elif value2 == 21:
                print('Winner Winner Chicken Dinner')
            else:
                print('Ooof, unlucky')

        elif value < 21:
            print('Stay')

        elif value == 21:
            print('Winner Winner Chicken Dinner')

        else:
            print('Ooof, unlucky')

        again = input('Type anything other than 0 to try again: ')
        print("Thanks for using our Blackjack Advisor!")

again = input("Want some BlackJack advice, just don't hit 0: ")
blackjack(again)

