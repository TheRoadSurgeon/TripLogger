import unittest
import Trip
import Truck
import Driver





class TestTruck(unittest.TestCase):
    

    def test_truck(self):
        truck = Truck.Truck(1, "Volov", "VLN860", 2015, 100000)
        self.assertEqual(truck.TruckID, 2)
        self.assertEqual(truck.Make, "Volov")
        self.assertEqual(truck.Model, "VNL860")
        self.assertEqual(truck.Year, 2015)
        self.assertEqual(truck.Mileage, 100000)

   