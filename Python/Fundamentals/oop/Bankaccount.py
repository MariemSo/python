class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    
    def withdraw(self, amount):
        if amount <= (self.balance):
            self.balance -= amount
        else:
            self.balance -=5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance:$",self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.int_rate = self.balance*self.int_rate
        print (self.int_rate)
        return self
int_rate = 0.01
balance  = 0
account1=BankAccount(int_rate, balance)
account2=BankAccount(int_rate, balance)
account1.deposit(100).deposit(300).deposit(50).withdraw(90).yield_interest().display_account_info()
account2.deposit(800).deposit(20).withdraw(100).withdraw(500).withdraw(300).withdraw(50).yield_interest().display_account_info()