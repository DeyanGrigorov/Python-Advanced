class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        # elf.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    def calculate_expenses(self, *args):
        pass
