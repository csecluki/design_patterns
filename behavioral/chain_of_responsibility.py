"""
Chain of Responsibility pattern is a behavioral design pattern that allows multiple objects to handle a request
in a chain-like structure. Instead of the sender of a request knowing which object in the chain will handle the
request, it simply sends the request to the first object in the chain. The objects in the chain then decide among
themselves which object will handle the request. The objects are connected to each other in a linked list, forming
a chain, hence the name Chain of Responsibility.

Each object in the chain has a reference to its successor, and it only forwards the request to the successor if
it can't handle it. The chain continues until either an object in the chain handles the request or the end of
the chain is reached. This allows for loose coupling between objects, as they don't need to know the details
of their successors in the chain.

In the Chain of Responsibility pattern, there are three main components: the Handler, the Client, and the Request.
The Handler is an abstract class that defines a common interface for all handlers in the chain. The Client is the
object that initiates the request and sends it to the first handler in the chain. The Request is an object that
encapsulates the information about the request being made.
"""


import enum


class PizzaSize(enum.Enum):

    SMALL = 10
    MEDIUM = 15
    LARGE = 20


class PizzaTopping(enum.Enum):

    MUSHROOM = 1
    PEPPERONI = 2
    EXTRA_CHEESE = 3


class Pizza:

    def __init__(self, size: PizzaSize, toppings: list[PizzaTopping]):
        self.size = size
        self.toppings = toppings

    def get_cost(self) -> int:
        return self.size.value + sum(topping.value for topping in self.toppings)


class PizzaOrderHandler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, pizza: Pizza) -> int:
        if self.successor is not None:
            return self.successor.handle(pizza)
        return 0


class DiscountHandler(PizzaOrderHandler):

    def handle(self, pizza: Pizza) -> int:
        if pizza.size == PizzaSize.LARGE and PizzaTopping.EXTRA_CHEESE in pizza.toppings:
            return 2
        return super().handle(pizza)


class CouponHandler(PizzaOrderHandler):

    def handle(self, pizza: Pizza) -> int:
        if len(pizza.toppings) >= 3:
            return 1
        return super().handle(pizza)


class DeliveryHandler(PizzaOrderHandler):

    def handle(self, pizza: Pizza) -> int:
        if pizza.size == PizzaSize.MEDIUM or pizza.size == PizzaSize.LARGE:
            return 3
        return super().handle(pizza)


def example():
    pizza = Pizza(PizzaSize.LARGE, [PizzaTopping.PEPPERONI, PizzaTopping.EXTRA_CHEESE])

    discount_handler = DiscountHandler()
    coupon_handler = CouponHandler(discount_handler)
    delivery_handler = DeliveryHandler(coupon_handler)

    total_cost = pizza.get_cost()
    discount = delivery_handler.handle(pizza)
    total_cost -= discount

    print(f"Total cost of pizza: {total_cost}")


if __name__ == "__main__":
    example()
