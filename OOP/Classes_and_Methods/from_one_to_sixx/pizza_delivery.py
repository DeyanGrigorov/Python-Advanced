from typing import Dict


class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def pizza_ordered(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        self.ordered = True
        str_ingredients = ', '.join([f"{i}: {quantity}" for i, quantity in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {str_ingredients} and the price will be {self.price}lv."
