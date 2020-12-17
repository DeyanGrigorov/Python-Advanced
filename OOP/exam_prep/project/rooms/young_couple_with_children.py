from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children = children
        self.appliances = [[TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]]
        for _ in range(len(children)):
            self.appliances.append([TV(), Fridge(), Laptop()])
        self.calculate_expense(*self.appliances, children)
