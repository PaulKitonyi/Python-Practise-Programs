
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return 'Invalid Transaction'

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

obj = BankAccount(0)
print(obj.deposit(500))
print(obj.withdraw(1500))

