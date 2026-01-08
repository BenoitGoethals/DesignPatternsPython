from typing import Protocol


class PaymentProcessor(Protocol):

    def pay(self, amount: float):
        pass


class OldBankSystem:
    def make_payment(self, euros):
        print(f"Betaling van €{euros} uitgevoerd via oud banksysteem")


class OldBankAdapter(PaymentProcessor):
    def __init__(self, old_bank: OldBankSystem):
        self._old_bank = old_bank

    def pay(self, amount: float):
        self._old_bank.make_payment(amount)


processor: PaymentProcessor = OldBankAdapter(OldBankSystem())
processor.pay(100.0)
