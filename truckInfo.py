"""
Date: 12/18/20224
@
A class file that creates truck details

"""

class Truck:
    def __init__(self, truckID: int, truckMiles: int, truckHome: int, truckMake: str, truckModel: str):
        self._TruckID = truckID 
        self._TruckMiles = truckMiles
        self._TruckHome = truckHome
        self._TruckMake = truckMake
        self._TruckModel = truckModel

    @property
    def TruckID(self):
        return self._TruckID
    
    @property
    def TruckMiles(self):
        return self._TruckMiles
    
    @property
    def TruckHome(self):
        return self._TruckHome
    
    @property
    def TruckMake(self):
        return self._TruckMake
    
    @property
    def TruckModel(self):
        return self._TruckModel