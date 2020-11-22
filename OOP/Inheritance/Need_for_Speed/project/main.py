from project.vehicle import Vehicle
from project.motorcycle import Motorcycle
from project.car import Car
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.cross_motorcycle import CrossMotorcycle
from project.family_car import FamilyCar

car = Car(70, 163)
print(car.drive(10))
print(car.fuel)