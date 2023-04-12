"""
The strategy pattern is a behavioral design pattern that allows you to dynamically switch algorithms or strategies
for a particular task or functionality. It is used when there are multiple ways to perform a task or achieve a goal,
and each approach has its pros and cons, and we want to switch between them at runtime.

In essence, the strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
This allows the algorithm to vary independently from clients that use it. Instead of implementing a single algorithm
directly in the code, the pattern creates a set of interchangeable algorithms, and allows the client to choose the
appropriate one at runtime.

The pattern consists of several key elements, including:
    *   The context: this is the object that is responsible for executing the strategy. It should be designed in a way
        that allows it to work with multiple strategies.

    *   The strategy: this is the interface or abstract class that defines the common methods for all algorithms.
        Each strategy represents a particular algorithm, and is implemented as a separate class.

    *   The concrete strategies: these are the classes that implement the various algorithms or strategies. Each
        strategy class should implement the methods defined by the strategy interface.
"""

from abc import ABC, abstractmethod
from typing import List


class PizzaTopping(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class PepperoniTopping(PizzaTopping):

    def get_description(self) -> str:
        return "Pepperoni"

    def get_cost(self) -> float:
        return 2.0


class MushroomTopping(PizzaTopping):

    def get_description(self) -> str:
        return "Mushroom"

    def get_cost(self) -> float:
        return 1.5


class PizzaSize(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class SmallSize(PizzaSize):

    def get_description(self) -> str:
        return "Small"

    def get_cost(self) -> float:
        return 10.0


class MediumSize(PizzaSize):

    def get_description(self) -> str:
        return "Medium"

    def get_cost(self) -> float:
        return 12.0


class Pizza:

    def __init__(self, toppings=None, size=None):
        self.toppings = toppings or []
        self.size = size

    def __str__(self) -> str:
        return self.get_description()

    def add_topping(self, topping: PizzaTopping) -> None:
        self.toppings.append(topping)

    def set_size(self, size: PizzaSize) -> None:
        self.size = size

    def get_description(self) -> str:
        topping_descriptions = [topping.get_description() for topping in self.toppings]
        toppings_string = ", ".join(topping_descriptions)
        size_description = self.size.get_description()
        return f"{size_description} pizza with {toppings_string}"

    def get_cost(self) -> float:
        topping_costs = [topping.get_cost() for topping in self.toppings]
        return self.size.get_cost() + sum(topping_costs)


class PizzaOrderingStrategy(ABC):

    @abstractmethod
    def order_pizza(self, toppings: List[PizzaTopping]):
        pass


class BasicPizzaOrderingStrategy(PizzaOrderingStrategy):

    def order_pizza(self, toppings: List[PizzaTopping]) -> Pizza:
        pizza = Pizza(size=SmallSize())
        for topping in toppings:
            pizza.add_topping(topping)
        return pizza


class CustomPizzaOrderingStrategy(PizzaOrderingStrategy):

    def __init__(self, size: PizzaSize):
        self.size = size

    def order_pizza(self, toppings: List[PizzaTopping] = None) -> Pizza:
        pizza = Pizza(size=self.size)
        for topping in toppings or []:
            pizza.add_topping(topping)
        return pizza


def example():
    pepperoni = PepperoniTopping()
    mushroom = MushroomTopping()

    basic_strategy = BasicPizzaOrderingStrategy()

    pizza = basic_strategy.order_pizza([pepperoni])
    print(pizza.get_description())
    print(pizza.get_cost())

    custom_strategy = CustomPizzaOrderingStrategy(MediumSize())

    pizza2 = custom_strategy.order_pizza([pepperoni, mushroom])
    print(pizza2)


if __name__ == '__main__':
    example()
