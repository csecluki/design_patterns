import enum
import itertools


class OrderStatus(enum.Enum):

    PREPARING = "Preparing"
    BACKING = "Backing"


class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, order):
        for observer in self._observers:
            observer.update(order)


class PizzaOrder(Subject):

    id_iter = itertools.count()

    def __init__(self):
        super().__init__()
        self.id_ = next(PizzaOrder.id_iter)
        self._order_status = None

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, status):
        self._order_status = status
        self.notify(self)


class Observer:

    def update(self, message):
        raise NotImplementedError


class Customer(Observer):

    def __init__(self, name):
        self._name = name

    def update(self, order: PizzaOrder):
        print(f"{self._name} received the message: Order {order.id_} status change to: {order.order_status.value}")


class Kitchen(Observer):

    def __init__(self):
        self._orders_in_progress = set()

    def update(self, order):
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
