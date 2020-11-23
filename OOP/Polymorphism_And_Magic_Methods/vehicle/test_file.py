# second zero test
from vehicle import Vehicle
from vehicle.Vehicle import Truck
import unittest


class VehiclesTests(unittest.TestCase):
    def test_second_zero(self):
        truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 64.5)


if __name__ == '__main__':
    unittest.main()