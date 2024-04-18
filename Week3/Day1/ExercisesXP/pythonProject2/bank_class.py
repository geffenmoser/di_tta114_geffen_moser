class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.owner}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds for Withdrawl")
            insufficient_withdraw_choice = input(f"Please enter '0' if you would like to cancel the withdrawl or enter '1' if you would like to withdraw your remaining balance of {self.balance}:")
            if insufficient_withdraw_choice == 1:
                self.transactions.append(f"Withdraw: {self.balance}")
                self.balance == 0
                print("Total Withdraw Approved")
                return 0
            elif insufficient_withdraw_choice == 0:
                print("Withdraw canceled:")
                break
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def get_balance(self):
        print(f"Your current balance is: {self.balance}")
        print("-------------")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Insufficient Funds for Transfer")
            insufficient_transfer_choice = input(
                f"Please enter '0' if you would like to cancel the transfer or enter '1' if you would like to transfer your remaining balance of {self.balance}:")
            if insufficient_transfer_choice_choice == 1:
                self.transactions.append(f"Withdraw: {self.balance}")
                deposit(other_account, self.balance)
                self.balance == 0
                print("Total Transfer Approved")
                return 0
            elif insufficient_withdraw_choice == 0:
                print("Transfer Canceled:")
                break
        else:
            withdraw(self, amount)
            deposit(other_account, amount)
            print(f"Transfer of {amount} from {self} to {other_account} was successful!")
