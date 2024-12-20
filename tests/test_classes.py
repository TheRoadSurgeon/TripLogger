"""
Date: 12/19/2024
@author: Hristian Tountchev
Test file to test functionality of classes.

"""

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
print(sys.path)

from src.Trip import Trip as Trip
from src.Truck import Truck as Truck
from src.Driver import Driver as Driver



class TestTruck(unittest.TestCase):
    
    def test_truck_full(self):
        truck = Truck(1, 350000, 604, "Volov", "VNL860", "The Company", "C788123", 2021)
        self.assertEqual(truck.TruckID, 1)
        self.assertEqual(truck.TruckMiles, 350000)
        self.assertEqual(truck.TruckHome, 604)
        self.assertEqual(truck.TruckMake, "Volov")
        self.assertEqual(truck.TruckModel, "VNL860")
        self.assertEqual(truck.IcIspName, "The Company")
        self.assertEqual(truck.IcIspNumber, "C788123")
        self.assertEqual(truck.TruckYear, 2021)
        

    def test_truck_small(self):
        truck = Truck(2, 25000)
        self.assertEqual(truck.TruckID, 2)
        self.assertEqual(truck.TruckMiles, 25000)
        self.assertEqual(truck.TruckHome, None)
        self.assertEqual(truck.TruckMake, None)
        self.assertEqual(truck.TruckModel, None)
        self.assertEqual(truck.IcIspName, None)
        self.assertEqual(truck.IcIspNumber, None)
        self.assertEqual(truck.TruckYear, None)

class TestDriver(unittest.TestCase):

    def test_driver_full(self):
        driver = Driver(1, "John", "Doe", "604")
        self.assertEqual(driver.DriverID, 1)
        self.assertEqual(driver.DriverFirstName, "John")
        self.assertEqual(driver.DriverLastName, "Doe")
        self.assertEqual(driver.DriverHome, "604")

    def test_driver_small(self):
        driver = Driver(2, "Jane", "Doe")
        self.assertEqual(driver.DriverID, 2)
        self.assertEqual(driver.DriverFirstName, "Jane")
        self.assertEqual(driver.DriverLastName, "Doe")
        self.assertEqual(driver.DriverHome, None)

class TestTrip(unittest.TestCase):
    
    def test_trip_full(self):
        trip = Trip(1, 1, 1, "12/18/2024 08:00", {"604": "Bedford Park IL", "436": "Toledo OH"}, {604: 30, 436: 100}, ["I-80", "I-90"])
        self.assertEqual(trip.TripID, 1)
        self.assertEqual(trip.TruckID, 1)
        self.assertEqual(trip.DriverID, 1)
        self.assertEqual(trip.Date, "12/18/2024 08:00")
        self.assertEqual(trip.LocationCodes, {"604": "Bedford Park IL", "436": "Toledo OH"})
        self.assertEqual(trip.MilesTraveled, {604: 30, 436: 100})
        self.assertEqual(trip.Roads, ["I-80", "I-90"])

if __name__ == "__main__":
    unittest.main()