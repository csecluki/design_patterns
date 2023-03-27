"""
The Facade pattern is a way to make things easier by providing a simple interface to a complicated system or part
of a system. It hides the complicated details behind an interface, making it easier for you to interact with the
system without worrying about all the inner workings.

Basically, the Facade acts as a middleman between you and the complicated part of the system. It simplifies the
interactions and lets you get the job done without having to deal with all the details.

The Facade pattern has three main parts:

    *   The Facade: This is the simple interface that you use to interact with the system. It's responsible for
        taking your requests and passing them along to the subsystem.
    *   The Subsystem: This is the complicated part of the system that the Facade is hiding. It's made up of
        a bunch of different pieces that work together to get things done.
    *   The Client: This is you! You're the one using the simple interface provided by the Facade to interact
        with the system.

The Facade pattern gives you a few benefits:

    *   It makes it easier to use a complicated system or subsystem by providing a simple interface.
    *   It hides the complexity of the subsystem, making it easier to understand and use.
    *   It helps to keep things loosely coupled, which makes the system more flexible and easier to maintain.
    *   It makes it easier to test the system, since you can test the Facade and the subsystem separately.

Overall, the Facade pattern is a useful tool for simplifying complicated systems and making them easier to use.
"""


class Pizza:
    def __init__(self, size: int, toppings: list[str]):
        self.size = size
        self.toppings = toppings
        self.is_ready = False

    def __str__(self) -> str:
        prefix = 'Ready to delivery: ' if self.is_ready else ''
        return f"{prefix}{self.size}cm pizza with: {', '.join(self.toppings)}"


class PizzaFacade:
    def __init__(self):
        self.oven = Oven()
        self.cutter = Cutter()
        self.box = Box()

    def order_pizza(self, size: int, toppings: list[str]) -> Pizza:
        pizza = Pizza(size, toppings)
        self.oven.bake(pizza)
        self.cutter.cut(pizza)
        self.box.package(pizza)
        pizza.is_ready = True
        return pizza


class Oven:

    @staticmethod
    def bake(pizza: Pizza) -> None:
        print(f"Baking {pizza.size}cm pizza with {', '.join(pizza.toppings)} toppings...")


class Cutter:

    @staticmethod
    def cut(pizza: Pizza) -> None:
        print(f"Cutting {pizza.size}cm pizza with {', '.join(pizza.toppings)} toppings...")


class Box:

    @staticmethod
    def package(pizza: Pizza) -> None:
        print(f"Packaging {pizza.size}cm pizza with {', '.join(pizza.toppings)} toppings...")


def example():
    pizza_facade = PizzaFacade()
    pizza = pizza_facade.order_pizza(12, ['cheese', 'pepperoni', 'mushrooms'])
    print(pizza)


if __name__ == '__main__':
    example()
