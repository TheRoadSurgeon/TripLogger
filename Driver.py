"""
Date: 12/18/2024
@author Hristian Tountchev
A class file that creates driver details
"""


# Class that keeps driver information nice an neat.
class Driver:
    def __init__(self, driverID: int, driverFirstName: str, driverLastName: str, driverHome: str):
        self._DriverID = driverID
        self._DriverFirstName = driverFirstName
        self._DriverLastName = driverLastName
        self._DriverHome = driverHome

    # Driver ID is an integer assigned by the company.
    @property
    def DriverID(self):
        return self._DriverID
    
    # Frist name of the driver.
    @property
    def DriverFirstName(self):
        return self._DriverFirstName
    
    # Last name of the driver.
    @property
    def DriverLastName(self):
        return self._DriverLastName
    
    # Driver home is a digit that is the indicator for which home base 
    # the driver starts their day in. 
    # Ex: 604 is Bedford Park, IL
    @property
    def DriverHome(self):
        return self._DriverHome 
    
    # The str helps with printing and logging.
    def __str__(self):
        return (
            f"Driver(ID: {self.DriverID}, Name: {self.DriverFirstName} {self.DriverLastName}, "
            f"Home Base: {self.DriverHome})"
        )
    
    # With eq with can do object comparisons.
    def __eq__(self, other):
        """Equality comparison for Driver objects."""
        if not isinstance(other, Driver):
            return False
        return self.DriverID == other.DriverID
    

