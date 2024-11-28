class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient funds')
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

ac1 = BankAccount(100)
ac1.deposit(100)
ac1.withdraw(50)
print(ac1.get_balance())
