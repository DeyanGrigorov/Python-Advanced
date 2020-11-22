# from abc import ABC, abstractmethod


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    # @abstractmethod
    def drive(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        if fuel_needed > self.fuel:
            return
        self.fuel -= fuel_needed
