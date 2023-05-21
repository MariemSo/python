#BankAccount Class
class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= (self.balance):
            self.balance -= amount
        else:
            self.balance -=amount-5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance:$",self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.int_rate = self.balance*self.int_rate
        return self

#user Class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)

    def display_user_balance(self):
        self.account.display_account_info()


herculus = User("chedi mola", "hirakel@gmail.com")
herculus.make_deposit(900)
herculus.make_withdrawal(500)
herculus.display_user_balance()
