from abc import ABC, abstractmethod
from enum import Enum, auto

"""
Creational:
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
        shapes = {ShapeType.CIRCLE: Circle, ShapeType.BOX: Box}
        # if shape_type == ShapeType.CIRCLE:
        #     return Circle()
        # elif shape_type == ShapeType.BOX:
        #     return Box()
        if shape_type not in shapes:
            raise ValueError('Unsupported shape')
        return shapes[shape_type]()


def test_factory():
    factory = ShapeFactory()
    shape = factory.create_shape(ShapeType.BOX)
    shape.draw()
