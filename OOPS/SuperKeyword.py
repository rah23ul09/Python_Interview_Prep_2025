class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def showDetails(self):
        print(f"Owner is {self.owner}")
        print(f"Balance is ${self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interestRate):
        super().__init__(owner, balance)
        self.interestRate = interestRate
        
    def showDetails(self):
        super().showDetails()
        print(f"Interest rate is {self.interestRate}%")


sa = SavingAccount("Rahul", 30000.00, 7.5)
sa.showDetails()