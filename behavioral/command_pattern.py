"""
The Command pattern is a design pattern that helps separate the object that performs an action (the receiver) from the object
that requests the action (the client). It uses a middleman object called the Command, which contains all the information
required to execute the action.

This pattern is especially useful when you need to create an undo/redo feature, queue up operations, or send requests to remote
machines.

The Command pattern is made up of four main parts:

    *   The Command object: It defines how to execute an operation and holds all the data needed for it. It doesn't rely on the
        receiver object and can work with any receiver.
    *   The Receiver object: It's responsible for actually executing the operation when the Command object is triggered. The
        Command object calls the necessary methods on the Receiver object.
    *   The Invoker object: It requests the Command object to perform an operation, without knowing what operation is being performed.
        It calls the execute method on the Command object.
    *   The Client: It creates the Command object and sets the receiver. The client also sets the invoker with the Command object.

By using the Command pattern, you can break down complex operations into simpler commands. It also enables you to add new commands
without changing existing code, as well as queue commands for later execution or log them for auditing purposes.
"""


from abc import ABC, abstractmethod


class Pizza:

    def __init__(self, name):
        self.name = name
        self.toppings = []

    def add_topping(self, topping: str) -> None:
        self.toppings.append(topping)
        print(f"{topping} added to {self.name} pizza")

    def remove_topping(self, topping: str) -> None:
        self.toppings.remove(topping)
        print(f"{topping} removed from {self.name} pizza")

    def get_toppings(self) -> list:
        return self.toppings

    def bake(self) -> None:
        print(f"{self.name} pizza is baking")

    def cut(self) -> None:
        print(f"{self.name} pizza is being cut")

    def box(self) -> None:
        print(f"{self.name} pizza is being boxed")


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class AddToppingCommand(Command):

    def __init__(self, pizza, topping):
        self.pizza = pizza
        self.topping = topping

    def execute(self) -> None:
        self.pizza.add_topping(self.topping)


class RemoveToppingCommand(Command):

    def __init__(self, pizza, topping):
        self.pizza = pizza
        self.topping = topping

    def execute(self) -> None:
        self.pizza.remove_topping(self.topping)


class BakePizzaCommand(Command):

    def __init__(self, pizza):
        self.pizza = pizza

    def execute(self) -> None:
        self.pizza.bake()


class CutPizzaCommand(Command):

    def __init__(self, pizza):
        self.pizza = pizza

    def execute(self) -> None:
        self.pizza.cut()


class BoxPizzaCommand(Command):

    def __init__(self, pizza):
        self.pizza = pizza

    def execute(self) -> None:
        self.pizza.box()


class PizzaChef:

    def __init__(self):
        self.commands = []

    def add_command(self, command: Command) -> None:
        self.commands.append(command)

    def execute_commands(self) -> None:
        for command in self.commands:
            command.execute()
        self.commands.clear()


def example():
    pepperoni_pizza = Pizza("Pepperoni")

    add_topping_command = AddToppingCommand(pepperoni_pizza, "Pepperoni")
    bake_command = BakePizzaCommand(pepperoni_pizza)
    cut_command = CutPizzaCommand(pepperoni_pizza)
    box_command = BoxPizzaCommand(pepperoni_pizza)

    chef = PizzaChef()
    chef.add_command(add_topping_command)
    chef.add_command(bake_command)
    chef.add_command(cut_command)
    chef.add_command(box_command)

    chef.execute_commands()

    print(pepperoni_pizza.get_toppings())


if __name__ == '__main__':
    example()
