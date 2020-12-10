from abc import ABC, abstractmethod
import unittest


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self._FUEL_CONSUMPTION) * distance
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    @abstractmethod
    def _FUEL_CONSUMPTION(self):
        pass


class Car(Vehicle, ABC):
    _FUEL_CONSUMPTION = 0.9

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle, ABC):
    _FUEL_CONSUMPTION = 1.6

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 2)

    def test_not_enough_fuel(self):
        # Act
        self.car.drive(40)

        # Assert
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_enough_fuel(self):
        self.car.drive(10)

        self.assertEqual(self.car.fuel_quantity, 71)

    def test_refuel(self):
        self.car.refuel(50)

        self.assertEqual(self.car.fuel_quantity, 150)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 2)

    def test_not_enough_fuel(self):
        # Act
        self.truck.drive(40)

        # Assert
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_enough_fuel(self):
        self.truck.drive(10)

        self.assertEqual(self.truck.fuel_quantity, 64)

    def test_refuel(self):
        self.truck.refuel(50)

        self.assertEqual(self.truck.fuel_quantity, 147.5)


if __name__ == '__main__':
    unittest.main()
