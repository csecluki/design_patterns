"""
The Observer Pattern is a design pattern in which an object, called the subject, maintains a list of its dependents,
called observers, and notifies them automatically of any changes to its state.

In this pattern, the subject keeps track of its observers and provides a way to attach and detach observers to/from
the subject. Whenever there is a change in the state of the subject, it notifies all of its observers by calling
a method on each observer.

The Observer Pattern is useful in situations where there is a one-to-many relationship between objects, such that
when one object changes state, all of its dependents are notified and updated automatically. This can help to decouple
the subject from its observers, as the subject does not need to know anything about its observers other than that
they implement a common interface.
"""


import enum
import itertools


class OrderStatus(enum.Enum):

    PREPARING = "Preparing"
    BACKING = "Backing"


class Observer:

    def update(self, message) -> None:
        raise NotImplementedError


class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class PizzaOrder(Subject):

    id_iter = itertools.count()

    def __init__(self):
        super().__init__()
        self.id_ = next(PizzaOrder.id_iter)
        self._order_status = None

    @property
    def order_status(self) -> OrderStatus:
        return self._order_status

    @order_status.setter
    def order_status(self, status: OrderStatus) -> None:
        self._order_status = status
        self.notify()


class Customer(Observer):

    def __init__(self, name: str):
        self._name = name

    def update(self, order: PizzaOrder) -> None:
        print(f"{self._name} received the message: Order {order.id_} status change to: {order.order_status.value}")


class Kitchen(Observer):

    def __init__(self):
        self._orders_in_progress = set()

    def update(self, order: PizzaOrder) -> None:
        self._orders_in_progress.add(order)
        print(f"New order received. Orders in progress: {', '.join(str(order.id_) for order in self._orders_in_progress)}")


def example():
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    customer3 = Customer("Jack")
    kitchen = Kitchen()

    order0 = PizzaOrder()
    order0.attach(customer1)
    order0.attach(customer2)
    order0.attach(kitchen)

    order1 = PizzaOrder()
    order1.attach(customer3)
    order1.attach(kitchen)

    order0.order_status = OrderStatus.PREPARING
    order1.order_status = OrderStatus.PREPARING

    order0.detach(customer2)

    order1.order_status = OrderStatus.BACKING
    order0.order_status = OrderStatus.BACKING


if __name__ == '__main__':
    example()
