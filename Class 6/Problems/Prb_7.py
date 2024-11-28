class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


account = BankAccount(100)
print(account.check_balance())

account.deposit(50)
print(account.check_balance())

account.withdraw(30)
print(account.check_balance())