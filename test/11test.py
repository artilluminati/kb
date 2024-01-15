class BankAccount:

    def __init__(self, balance):

        self._balance = balance

    def get_balance(self):

        return self._balance

    def _withdraw(self, amount):

        if amount <= self._balance:

            self._balance -= amount

            return f"Withdrawal successful. Remaining balance: {self._balance}"

        else:

            return "Insufficient funds."

account = BankAccount(1000)

print(account.get_balance())

print(account._withdraw(500))