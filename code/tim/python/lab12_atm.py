# Lab 12: ATM

transactions = []

class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1

    def check_balance(self):
        # Returns account balance
        balance = self.balance 
        return balance
        
    def deposit(self, amount):
        # Deposits the given amount to the account as long as it is a positive number, returning True.
        if amount > 0:            
            self.balance += amount
            transactions.append(f"Deposited - ${amount}. New balance - ${self.balance}.")
            return True
        else:
            return False
        
    def check_withdrawal(self, amount):
        # Returns True if the withdrawn amount won't put the account in the negative
        if amount < self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        # Withdraws the amount from the account and returns the amount
        self.balance -= amount
        print(f"New balance - ${self.balance}.")
        transactions.append(f"Withdrew - ${amount}. New balance - ${self.balance}.")


    def calc_interest(self):
        # Returns the amount of interest calculated on the account
        interest = self.balance * self.interest_rate
        print(interest)
        return interest

    def print_transactions(self):
        for transaction in transactions:
            print(transaction)

atm = ATM()  # Create an instance of our class
print("Welcome to the ATM where all the finances are made up and the money doesn't matter!")

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Transactions',
    '6': 'Exit'
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input(
        '\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance()  # Call the check_balance() method
        print(f'Your balance is - ${balance}')

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount)  # Call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew - ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest()  # Call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Transactions':
        transactions = atm.print_transactions()
        print(f'End of transaction log.')
    
    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')