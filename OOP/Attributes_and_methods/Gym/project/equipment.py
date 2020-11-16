class Equipment:

    autoincrement_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.autoincrement_id
        Equipment.autoincrement_id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.autoincrement_id

