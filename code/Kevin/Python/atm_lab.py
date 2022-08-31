'''
Program for ???
'''

#Im
import time


class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        # Returns account balance
        return self.balance

    def deposit(self, amount):
        # deposits he given amount to the account
        if amount >= 0.01:
            self.balance += amount
            return True
        else:
            return False

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount

    def calc_interest(self):
        interest = round((self.balance * 1.0003) - self.balance, 6)
        return interest


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input(
        '\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}');time.sleep(1.5)

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount)  # call the deposit(amount) method
        if not success:
            print("Deposit amount must be at least 1 cent.");time.sleep(1.5)
        else:
            print(f'Deposited ${amount}');time.sleep(1.5)

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print('Insufficient funds');time.sleep(1.5)
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}');time.sleep(1.5)

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest');time.sleep(1.5)

    elif command == 'Exit':
        print("Goodbye!");time.sleep(1.5)
        break

    else:
        print('Command not recognized');time.sleep(1.5)