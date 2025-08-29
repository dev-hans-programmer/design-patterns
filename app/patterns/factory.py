from abc import ABC, abstractmethod
from enum import Enum, auto

"""
Factory Pattern provides a way to create objects without exposing the creation 
logic to the client.
Instead of calling a class constructor directly, you use a factory method that 
decides which object to create.

Use cases:
    1. Database drivers - Factory decides whether to give you a MySQLConn
    , PostgresConn based on db type
    2. Payment Systems, you request a PaymentProcessor("paypal"), and the 
    factory returns a PayPalProcessor object.
"""


class ShapeType(Enum):
    CIRCLE = auto()
    BOX = auto()


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing circle')


class Box(Shape):
    def draw(self):
        print('Drawing box')


class ShapeFactory:
    def create_shape(self, shape_type: ShapeType):
        if shape_type == ShapeType.CIRCLE:
            return Circle()
        elif shape_type == ShapeType.BOX:
            return Box()


def test_factory():
    factory = ShapeFactory()
    shape = factory.create_shape(ShapeType.CIRCLE)
    shape.draw()
