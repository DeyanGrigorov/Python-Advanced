from project.rooms import room
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for r in self.rooms:
            total += r.expenses + r.room_cost
        # total = sum(r.expenses * 30 + r.room_cost for r in self.rooms)
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        array = []
        for r in self.rooms:
            if r.budget >= r.expenses + r.room_cost:
                # new_budget = r.budget - (r.expenses + r.room_cost)
                r.budget -= r.expenses + r.room_cost

                array.append(f'{r.family_name} paid {r.expenses+r.room_cost:.2f}$ and have {r.budget:.2f}$ left.')

            else:
                array.append(f'{r.family_name} does not have enough budget and must leave the hotel.')
        return '\n'.join(array)

    def status(self):
        total_people = 0
        for p in self.rooms:
            total_people += p.members_count
        return total_people

