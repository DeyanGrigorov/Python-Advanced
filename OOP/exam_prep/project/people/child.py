class Child:
    def __init__(self, food_cost, *toy_cost):
        self.cost = food_cost + sum(toy_cost)

