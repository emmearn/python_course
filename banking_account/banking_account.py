class Account:
    def __init__(self, name, account):
        self.name = name
        self.account = account


class BankAccount(Account):
    def __init__(self, name, account, amount):
        super().__init__(name, account)
        self.__amount = amount

    @property
    def amount(self):
        print("I'm calling the getter method")
        return self.__amount

    @amount.setter
    def amount(self, amount):
        print("I'm calling the setter method")
        self.__amount = amount

    def withdraw(self, amount):
        self.__amount -= amount

    def deposit(self, amount):
        self.__amount += amount

    def to_string(self):
        print(f'{self.name} {self.account} ${self.amount}')


banking_account1 = BankAccount('Mario Rossi', 123, 0)
banking_account2 = BankAccount('Mario Bianchi', 124, 0)

banking_account1.amount = 10000  # I'm calling the setter method
banking_account2.amount = 6000  # I'm calling the setter method

banking_account1.to_string()  # I'm calling the getter method  # Mario Rossi 123 $10000
banking_account2.to_string()  # I'm calling the getter method  # Mario Bianchi 124 $6000

for count in range(1, 4):
    banking_account1.withdraw(1000)

banking_account1.deposit(100)

banking_account1.to_string()  # I'm calling the getter method  # Mario Rossi 123 $7100

for count in range(1, 100):
    banking_account2.withdraw(10 + count)

banking_account2.to_string()  # I'm calling the getter method  # Mario Bianchi 124 $60

print(banking_account1._BankAccount__amount)  # oops
