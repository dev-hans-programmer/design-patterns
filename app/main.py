from app.patterns.factory import ShapeFactory, ShapeType
from app.patterns.singleton import Logger
from app.patterns.strategy import (
    CreditCardPayment,
    PaymentProcessor,
    PaypalPayment,
)


def test_singleton():
    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)


def test_factory():
    factory = ShapeFactory()
    shape = factory.create_shape(ShapeType.CIRCLE)
    shape.draw()


def test_strategy():
    payment_processor = PaymentProcessor(CreditCardPayment())
    payment_processor.pay()

    # pay using paypal
    payment_processor.set_strategy(PaypalPayment())
    payment_processor.pay()


if __name__ == '__main__':
    test_singleton()
    test_factory()
    test_strategy()
