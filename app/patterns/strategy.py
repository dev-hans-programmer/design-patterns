from abc import ABC, abstractmethod

"""
It is used when we have multiple options, and we have to choose one 
dynamically at runtime without changing the code of the client

Use cases
    1. When we have different ways to calculate payment
    2. Diffrent ways to sort data

Instead of hardcoding if/else everywhere , we can encapsulate these strategies
into separate classes.

Promotes Open/Closed Principle

"""


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self):
        print('Paid using credit card')


class PaypalPayment(PaymentStrategy):
    def pay(self):
        print('Paid using paypal')


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def pay(self):
        self._strategy.pay()
