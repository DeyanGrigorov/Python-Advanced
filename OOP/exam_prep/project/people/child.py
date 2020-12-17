class Child:
    def __init__(self, food_cost, *toy_cost):
        self.cost = food_cost + sum(toy_cost)

    def get_monthly_expense(self):
        return self.cost * 30
