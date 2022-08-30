
class Wallet:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.money_spent = 0

    def spend_money(self, money_spent):
        if self.balance >= money_spent:
            self.balance -= money_spent
            self.money_spent += money_spent
            return True
        return False


name = input('What is your name: ')
balance = int(input("How much money do you have on you? "))

wallet = Wallet(name, balance)

print(f"\nYou, {wallet.name} has ${wallet.balance}")


print('\nYou got a craving for swedish fish')
cost  = int(input("each Swedish Fish bag costs $1. How many do you want to buy? "))


if wallet.spend_money(cost) == True:
    print(f"\nYou spent ${wallet.money_spent} and have a remaining balance of ${wallet.balance}")
else:
    print(f"\nYou tried to spend ${cost}, but you only have ${wallet.balance} available")