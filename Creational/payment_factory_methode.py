from abc import ABC, abstractmethod


class PaymentProvider(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class CardPayment(PaymentProvider):
    def pay(self, amount: float) -> bool:
        print(f"Charging credit card: €{amount}")
        return True


class PaypalPayment(PaymentProvider):
    def pay(self, amount: float) -> bool:
        print(f"Processing PayPal payment: €{amount}")
        return True


class BankTransferPayment(PaymentProvider):
    def pay(self, amount: float) -> bool:
        print(f"Initiating bank transfer: €{amount}")
        return True


class PaymentFactory:
    @staticmethod
    def create(method: str) -> PaymentProvider:
        if method == "card":
            return CardPayment()
        elif method == "paypal":
            return PaypalPayment()
        elif method == "bank":
            return BankTransferPayment()
        else:
            raise ValueError(f"Unsupported payment method: {method}")


class PaymentRequest:
    pay_type: str
    amount: float


# @app.post("/pay")
def pay(request: PaymentRequest):
    provider = PaymentFactory.create(request.pay_type)
    provider.pay(request.amount)
    return {"status": "ok"}
