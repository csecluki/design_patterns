class Pizza:

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):

    def prepare(self):
        print("Preparing cheese pizza...")

    def bake(self):
        print("Baking cheese pizza...")

    def cut(self):
        print("Cutting cheese pizza...")

    def box(self):
        print("Boxing cheese pizza...")


class PepperoniPizza(Pizza):

    def prepare(self):
        print("Preparing pepperoni pizza...")

    def bake(self):
        print("Baking pepperoni pizza...")

    def cut(self):
        print("Cutting pepperoni pizza...")

    def box(self):
        print("Boxing pepperoni pizza...")


class PizzaFactory:

    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")


def example():
    pizza_factory = PizzaFactory()

    cheese_pizza = pizza_factory.create_pizza("cheese")
    cheese_pizza.prepare()
    cheese_pizza.bake()
    cheese_pizza.cut()
    cheese_pizza.box()

    pepperoni_pizza = pizza_factory.create_pizza("pepperoni")
    pepperoni_pizza.prepare()
    pepperoni_pizza.bake()
    pepperoni_pizza.cut()
    pepperoni_pizza.box()


if __name__ == "__main__":
    example()
