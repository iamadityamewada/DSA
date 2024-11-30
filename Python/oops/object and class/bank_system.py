class Bank_account:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = int(input("Enter Amount to deposit: "))
        self.balance += amount
        print("Deposit Successfully")    

    def withdraw(self):
        amount = int(input("Enter Amount to deposit"))
        if self.balance - amount < 0:
           print(f"Enter Amount equal to {self.balance} or less")
        else:
           self.balance -= amount   
           print("withdrawal Successfully")
           print("updated balance: ", self.balance)

    def show_balance(self):
        print("Balance: ", self.balance)     


account = Bank_account()
account.show_balance()