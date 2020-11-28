from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f'Squeak'

    def feed(self, food):
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f'Woof!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f'Meow'

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f'ROAR!!!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
