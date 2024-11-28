class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("123456", 100)
print(account.get_balance())

account.deposit(100)
print(account.get_balance())

account.withdraw(50)
print(account.get_balance())