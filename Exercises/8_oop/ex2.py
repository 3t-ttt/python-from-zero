class BankAccount:

    def __init__(self, name, password, balance = 0, account_type = "normal"):
        self.name = name
        self.password = password
        self.balance = balance
        self.account_type = account_type

    def withdraw(self, amount):
        if amount > self.balance:
            return "amount must be less than balance"
        else:
            self.balance -= amount
            return f"{amount} withdrawn. New balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposit. New balance is {self.balance}"

class VIPBankAccount(BankAccount):
    def __init__(self, name, password, balance):
        if balance >= 1e6:
            super().__init__(name, password, balance, account_type="vip")
        else:
            super().__init__(name, password, balance, account_type="normal")

my_acc = BankAccount("tintt", "hellopython")
my_acc.deposit(1000)
print(my_acc.balance)
my_acc.withdraw(2000)
print(my_acc.withdraw(2000))


