from bank_account.bank_account import BankAccount


class BankAccountsManager:
    @staticmethod
    # the type and the return type are optional
    def transfer(from_account: BankAccount, to_account: BankAccount, amount) -> None:
        from_account.withdraw(amount)
        to_account.deposit(amount)


c1 = BankAccount('Mario Rossi', 123, 2000)
c2 = BankAccount('Mario Bianchi', 124, 5000)

c1.to_string()
c2.to_string()

BankAccountsManager.transfer(c1, c2, 500)

c1.to_string()
c2.to_string()
