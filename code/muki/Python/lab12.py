# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

from datetime import datetime
dtg = datetime.now()
dd = dtg.day
mm = dtg.month
yyyy = dtg.year

# #   Commented out for testing time. 
# balance = 0
# interest = .01
txlist = []
class ATM:
    def __init__(self, balance=0, interest=0.001):
        self.balance = balance
        self.interest = interest

    def check_balance(self):
        return self.balance
    
    def deposit(self, dep):
        self.balance = self.balance + dep

    def check_withdrawl(self, amount):
        if amount <= self.balance:
            return True
        elif amount > self.balance:
            return False
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def calc_interest(self):
        return self.balance * self.interest

    def logg(self, list, tx):
        list = list.append(tx)

    def print_transactions(self, list):
        print(list)
        

    









atm = ATM() # create an instance of our class
print('\nWelcome to the ATM\n')
while True:
    command = input('Enter a command:\nbalance\ndeposit\nwithdraw\ninterest\ntransaction log\nhelp\nexit\n\n>')
    
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'\nYour balance is ${balance}\n')
    elif command == 'deposit':
        amount = round(float(input('How much would you like to deposit? ')))
        atm.deposit(amount) # call the deposit(amount) method
        atm.logg(txlist, f'Deposited ${amount}')
        print(f'\nDeposited ${amount}\n')
    elif command == 'withdraw':
        amount = round(float(input('How much would you like to withdraw? ')))
        if atm.check_withdrawl(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.logg(txlist, f'Withdrew ${amount}')
            print(f'\nWithdrew ${amount}\n')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        atm.logg(txlist, f'Accumulated ${amount} in interest')
        print(f'\nAccumulated ${round(amount)} in interest\n')
    elif command == 'transaction log':
        atm.print_transactions(f'{txlist}\n')
    elif command == 'help':
        print('\nAvailable commands:')
        print('\nbalance  - get the current balance')
        print('\ndeposit  - deposit money')
        print('\nwithdraw - withdraw money')
        print('\ninterest - accumulate interest')
        print('\ntransaction log - displays log of transactions') # added for version 2
        print('\nexit     - exit the program\n\n')
    elif command == 'exit':
        break
    else:
        print('\nCommand not recognized, please try again.\n')
