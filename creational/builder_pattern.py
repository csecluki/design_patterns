"""
The Builder pattern is a design pattern used in software engineering to simplify the creation of complex objects. It separates
the construction of an object from its representation, allowing for the creation of various representations of the same object
with the same construction process.

The pattern consists of several key components, including the Director, Builder, Concrete Builder, and Product. The Director
is responsible for controlling the construction process and works with the Builder interface to build the object. The Builder
interface defines the methods for creating the parts of the complex object, and the final method for assembling the parts into
the finished product. The Concrete Builder class implements the Builder interface and provides the specific implementation for
building the parts of the complex object. Finally, the Product is the complex object that is being built.

The benefits of using the Builder pattern include the ability to break down the construction of complex objects into simpler
steps, enabling the creation of multiple representations of the same complex object, greater control over the construction
process, and the ability to modify the construction process without affecting the object itself.
"""


class Pizza:
    def __init__(self):
        self.base = None
        self.toppings = []
        self.cheeses = []

    def __repr__(self):
        return f"{self.base.capitalize()} pizza with {', '.join(self.toppings)} and {', '.join(self.cheeses)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_base(self, base: str):
        self.pizza.base = base
        return self

    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)
        return self

    def add_cheese(self, cheese: str):
        self.pizza.cheeses.append(cheese)
        return self

    def bake(self) -> Pizza:
        return self.pizza


def example():
    my_pizza = PizzaBuilder()\
        .set_base('thin crust')\
        .add_topping('mushrooms')\
        .add_cheese('mozzarella')\
        .bake()
    print(my_pizza)


if __name__ == '__main__':
    example()
