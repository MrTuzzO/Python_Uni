class BankAccount:
    interest_rate = .3

    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def create_account(cls, balance):
        return cls(balance)

    @staticmethod
    def get_interest_rate():
        return BankAccount.interest_rate

account = BankAccount.create_account(1000)
print(account.balance)
print(BankAccount.get_interest_rate())
