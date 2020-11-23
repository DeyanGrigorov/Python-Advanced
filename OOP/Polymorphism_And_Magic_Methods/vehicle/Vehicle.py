from abc import ABC, abstractmethod


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

