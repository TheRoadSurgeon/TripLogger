"""
Date: 12/18/2024
@author Hristian Tountchev
A class file that creates trip object.
This object should keep track of information of a given trip.
On a trip we need to keep track of:
            driver(Name/ID); truck(ID); date(trip should last one day); 
            location(list of number code Ex: 604); miles traveled(list); major roads used(list).
"""

from datetime import datetime

class Trip:
    def __init__(self, tripID: int, truckID: int, driverID: int, date: str, locationCodes: dict, milesTraveled: dict, roads: list):
        self._TripID = tripID
        self._TruckID = truckID
        self._DriverID = driverID
        try:
            datetime.strptime(date, "%m/%d/%Y %H:%M")
        except ValueError:
            raise ValueError(f"Invalid date format: {date}, should be MM/DD/YYYY HH:MM")
        self._Date = date
        # Location codes is a dictionary of all the codes that the drivers was in with the respective location 
        # Ex: key: 604 value: Bedford Park IL, key: 436 value: Toledo OH
        self._LocationCodes = locationCodes 
        self._MilesTraveled = milesTraveled # MilesTraveled is a dictionary Ex: key: 604 value: 30 (miles)
        self._Roads = roads

    @property
    def TripID(self):
        return self._TripID
    
    @property
    def TruckID(self):
        return self._TruckID

    @property
    def DriverID(self):
        return self._DriverID
    
    @property
    def Date(self):
        return self._Date
    
    @property 
    def LocationCodes(self):
        return self._LocationCodes
    
    @property
    def MilesTraveled(self):
        return self._MilesTraveled
    
    @property
    def Roads(self):
        return self._Roads
    
    def __str__(self):
        return (
            f"Trip ID: {self.TripID}, Truck ID: {self.TruckID}, Driver ID: {self.DriverID}, 
            Date: {self.Date}, Location Codes: {self.LocationCode}, 
            Miles Traveled: {self.MilesTraveled}, Roads: {self.Roads}"
        )
    
    def __repr__(self):
        return (
            f"Trip(TripID={self.TripID}, TruckID={self.TruckID}, DriverID={self.DriverID}, Date={self.Date})"
        )
        
    def __eq__(self, value):
        if not isinstance(value, Trip):
            return False
        return self.TripID == value.TripID