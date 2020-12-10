from typing import List


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name, people: List[Person]):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group('Some_Name', people=self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __str__(self):
        all_names = ', '.join(map(str, self.people))
        return f"{__class__.__name__} {self.name} with members {all_names}"

    def __getitem__(self, key):
        return f"Person {key}: {self.people[key]}"



p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)