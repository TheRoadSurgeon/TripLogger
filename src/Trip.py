"""
Date: 12/18/2024
@author Hristian Tountchev
A class file that creates trip object.
This object should keep track of information of a given trip.
On a trip we need to keep track of:
            driver(Name/ID); truck(ID); date(trip should last one day); 
            location(list of number code Ex: 604); miles traveled(list); major roads used(list).
"""
from dataclasses import dataclass, field
from typing import Optional, Dict, List

@dataclass
class Trip:
    trip_id: Optional[int] = None  # Primary key, auto-incremented
    truck_id: int = 0  # Foreign key to Truck table
    driver_id: int = 0  # Foreign key to Driver table
    
    start_date: Optional[str] = None  # e.g., "YYYY-MM-DD"
    end_date: Optional[str] = None  # e.g., "YYYY-MM-DD"
    start_location: Optional[str] = None
    end_location: Optional[str] = None

    location_codes: Dict[int, str] = field(default_factory=dict)  # e.g., {604: "Bedford Park IL"}
    miles_traveled: int = 0  # Total miles traveled
    roads: List[str] = field(default_factory=list)  # Major roads traveled

    rate: Optional[float] = None  # Per-mile or flat rate (not in use yet)
    total_payment: Optional[float] = None  # Computed total payment (not in use yet)
    load_description: Optional[str] = None  # Description of cargo/load
    cargo_weight: Optional[float] = None  # Weight of the cargo
    fuel_used: Optional[float] = None  # Fuel consumed (gallons/liters)

    ic_isp_name: Optional[str] = None  # Independent Contractor/Service Provider name
    ic_isp_number: Optional[str] = None  # IC/ISP identification number


    def __str__(self):
        """Custom string representation."""
        return (
            f"Trip(ID: {self.trip_id}, Truck: {self.truck_id}, Driver: {self.driver_id}, "
            f"Start: {self.start_date} ({self.start_location}), End: {self.end_date} ({self.end_location}), "
            f"Miles: {self.miles_traveled}, Roads: {self.roads})"
        )