# without inheritance
"""class CreditCardPayment:

    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:

    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")"""

# with inheritance

import random


class BankTransferPayment:

    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

class CreditCardPayment(BankTransferPayment):

    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(BankTransferPayment):

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

def make_payment(method, amount):
    method.process_payment(amount)

if __name__ == "__main__":
    payment1 = CreditCardPayment()
    make_payment(payment1, 100)
    payment2 = PayPalPayment()
    make_payment(payment2, 200)
    payment3 = BankTransferPayment()
    make_payment(payment3, 300)
    payment_methods = [CreditCardPayment(), PayPalPayment(), BankTransferPayment()]
    # payment_methods = [payment1, payment2, payment3] # this also works
    for payment_method in payment_methods:
        make_payment(payment_method, random.randint(100,200))