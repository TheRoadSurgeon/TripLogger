"""
Date: 12/18/20224
@ Hristian Tountchev
A class file that creates truck details
"""
# Truck class to keep truck information nice and neat.
class Truck:
    def __init__(self, truckID: int, truckMiles: int, truckHome: int, truckMake: str, truckModel: str):
        self._TruckID = truckID 
        self._TruckMiles = truckMiles
        self._TruckHome = truckHome
        self._TruckMake = truckMake
        self._TruckModel = truckModel

    # Truck ID generally assigned by the company.
    @property
    def TruckID(self):
        return self._TruckID
    
    # Trucker's current odometer mileage.
    @property
    def TruckMiles(self):
        return self._TruckMiles
    
    # Truck home is a digit that is the indicator for which home base 
    # the truck starts their day in. 
    # Ex: 604 is Bedford Park, IL
    @property
    def TruckHome(self):
        return self._TruckHome
    
    # Make is the company of the truck.
    # Ex: Volov
    @property
    def TruckMake(self):
        return self._TruckMake
    
    # Model is the type of truck.
    # Ex: VNL 860
    @property
    def TruckModel(self):
        return self._TruckModel