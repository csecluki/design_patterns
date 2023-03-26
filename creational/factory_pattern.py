"""
The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created. In other words, it provides a way to create objects
without specifying the exact class of object that will be created.

The Factory pattern is useful when the code needs to work with objects that have similar behavior but different implementations.
By using the Factory pattern, the code can be designed to work with a common interface, while still being able to create objects
of different types as needed.

The key elements of the Factory Design Pattern are the Factory class, which provides the interface for creating objects, and
the Concrete classes, which are the actual classes that are created by the Factory. The Factory class can be either abstract
or concrete, depending on the specific needs of the code.

The Factory pattern can be implemented in several ways, such as Simple Factory, Factory Method, and Abstract Factory. In Simple
Factory, a single factory class is used to create all the different types of objects. In Factory Method, each subclass has its
own factory method that creates its own type of object. In Abstract Factory, a set of related factory classes is used to create
families of related objects.
"""


import enum
from abc import ABC


class PizzaType(enum.Enum):

    CHEESE = enum.auto()
    PEPPERONI = enum.auto()


class Pizza(ABC):

    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        pass

    def cut(self) -> None:
        pass

    def box(self) -> None:
        pass


class CheesePizza(Pizza):

    def prepare(self) -> None:
        print("Preparing cheese pizza...")

    def bake(self) -> None:
        print("Baking cheese pizza...")

    def cut(self) -> None:
        print("Cutting cheese pizza...")

    def box(self) -> None:
        print("Boxing cheese pizza...")


class PepperoniPizza(Pizza):

    def prepare(self) -> None:
        print("Preparing pepperoni pizza...")

    def bake(self) -> None:
        print("Baking pepperoni pizza...")

    def cut(self) -> None:
        print("Cutting pepperoni pizza...")

    def box(self) -> None:
        print("Boxing pepperoni pizza...")


class PizzaFactory:

    @staticmethod
    def create_pizza(pizza_type: PizzaType) -> Pizza:
        match pizza_type:
            case PizzaType.CHEESE:
                return CheesePizza()
            case PizzaType.PEPPERONI:
                return PepperoniPizza()


def example():
    pizza_factory = PizzaFactory()

    cheese_pizza = pizza_factory.create_pizza(PizzaType.CHEESE)
    cheese_pizza.prepare()
    cheese_pizza.bake()
    cheese_pizza.cut()
    cheese_pizza.box()
    print()

    pepperoni_pizza = pizza_factory.create_pizza(PizzaType.PEPPERONI)
    pepperoni_pizza.prepare()
    pepperoni_pizza.bake()
    pepperoni_pizza.cut()
    pepperoni_pizza.box()


if __name__ == "__main__":
    example()
