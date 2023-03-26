"""
The Adapter Pattern is a design pattern that allows two incompatible interfaces to work together by creating a third class
that acts as a bridge between them. It is used when the interface of an existing class does not meet the needs of the client
and a new interface is required.

The pattern consists of three main components: the Target interface, the Adaptee class, and the Adapter class. The Target
interface defines the operations that the client requires, while the Adaptee class provides the implementation of those
operations. The Adapter class adapts the Adaptee class to the Target interface.

The Adapter class has a reference to an instance of the Adaptee class, and implements the Target interface. It acts as
a wrapper around the Adaptee class, translating calls to the Target interface into calls to the Adaptee interface.

There are two types of Adapter Pattern: the Class Adapter Pattern and the Object Adapter Pattern. In the Class Adapter Pattern,
the Adapter class extends the Adaptee class and implements the Target interface. In the Object Adapter Pattern, the Adapter
class has a reference to an instance of the Adaptee class and implements the Target interface.

The Adapter Pattern allows existing classes to be reused without modifying their code, and allows clients to work with classes
that have incompatible interfaces. It is commonly used in software systems where different subsystems or components have
different interfaces and need to be integrated.
"""
from abc import ABC, abstractmethod


class Pizza(ABC):

    @staticmethod
    @abstractmethod
    def make_pizza() -> str:
        raise NotImplementedError()

class MargheritaPizza(Pizza):

    @staticmethod
    def make_pizza() -> str:
        return "Making Margherita pizza"

class PepperoniPizza(Pizza):

    @staticmethod
    def make_pizza() -> str:
        return "Making Pepperoni pizza"

class Calzone:

    @staticmethod
    def make_calzone() -> str:
        return "Making Calzone"

class CalzoneAdapter(Pizza):

    def __init__(self, calzone: Calzone):
        self.calzone = calzone

    def make_pizza(self) -> str:
        return self.calzone.make_calzone()


def example():
    margherita = MargheritaPizza()
    pepperoni = PepperoniPizza()
    calzone = Calzone()
    calzone_adapter = CalzoneAdapter(calzone)

    pizzas = [margherita, pepperoni, calzone_adapter]

    for pizza in pizzas:
        print(pizza.make_pizza())


if __name__ == '__main__':
    example()
