class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

# from Ex_5 import BankAccount
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_funds(self):
        return sum(account.get_balance() for account in self.accounts)


ac1 = BankAccount(101, 1000)
ac2 = BankAccount(102, 1500)
ac3 = BankAccount(103, 2000)

bankFund = Bank()

bankFund.add_account(ac1)
bankFund.add_account(ac2)
bankFund.add_account(ac3)

print(f"Total Founds: {bankFund.total_funds()}")
