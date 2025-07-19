from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self):
        print("Transaction completed. Receipt generated")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using credit card.")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using UPI.")


p1 = CardPayment()
p1.pay(1233)
p1.receipt()

p2 = UPIPayment()
p2.pay(1321)
p2.receipt()