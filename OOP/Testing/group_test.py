from typing import List


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __str__(self):
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


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('Deyan', 'Grigorov')

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertIn('Deyan', result)
        self.assertEqual(result, 'Deyan Grigorov')

    def test_custom_add(self):
        person_2 = Person('Test', 'Testov')
        person_3 = self.person_1 + person_2
        self.assertEqual(person_3.name, 'Deyan')
        self.assertEqual(person_3.surname, 'Testov')


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('Deyan', 'Grigorov')
        self.person_2 = Person('Test', 'Testov')
        self.group = Group('test', [self.person_1, self.person_2])

    def test_custom_len(self):
        self.assertEqual(len(self.group), 2)

    def test_custom_add(self):
        person_3 = Person('3', '3')
        group_2 = Group('test2', [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_get_item(self):
        result = self.group[1]
        self.assertIn('Test', result)
        self.assertEqual(result, 'Person 1: Test Testov')

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn('Deyan', result)
        self.assertIn('Test', result)
        all_names = ', '.join(['Deyan Grigorov', 'Test Testov'])
        result_2 = f"Group test with members {all_names}"
        self.assertEqual(result, result_2)

    def test_custom_get_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]


if __name__ == '__main__':
    unittest.main()