class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def get_needs():
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

