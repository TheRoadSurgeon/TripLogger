"""
Date: 12/18/2024
@author Hristian Tountchev
A class file that creates truck details
"""
from dataclasses import dataclass, field
from typing import Optional
# Truck class to keep truck information nice and neat.
@dataclass
class Truck:
    truck_id: Optional[int] = None  # Primary key, auto-incremented
    external_truck_id: Optional[str] = None  # External ID from another company/system
    vin: str = ""  # Vehicle Identification Number, unique
    license_plate_number: Optional[str] = None
    truck_make: Optional[str] = None
    truck_model: Optional[str] = None
    truck_year: Optional[int] = None  # e.g., 2020
    truck_type: Optional[str] = None  # e.g., "tractor", "flatbed"
    ic_isp_name: Optional[str] = None  # Independent Contractor/ISP name
    ic_isp_number: Optional[str] = None  # IC/ISP identification number
    color: Optional[str] = None
    
    ownership_status: Optional[str] = None  # e.g., "owned", "leased", "rented"
    registered_state: Optional[str] = None  # e.g., "CA"
    registration_expiration_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    
    insurance_policy_number: Optional[str] = None
    insurance_expiration_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    ifta_account_number: Optional[str] = None  # Fuel tax account number
    
    odometer_reading: Optional[float] = None
    odometer_last_updated_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    
    fuel_type: Optional[str] = None  # e.g., "diesel"
    fuel_efficiency_rating: Optional[float] = None  # Fuel efficiency rating
    gvwr: Optional[str] = None  # Gross Vehicle Weight Rating
    cargo_capacity: Optional[str] = None  # Cargo capacity
    
    assigned_driver_id: Optional[int] = None  # Which driver the truck is assign to
    
    purchase_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    warranty_expiration_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    last_service_date: Optional[str] = None  # Stored as "YYYY-MM-DD"
    maintenance_notes: Optional[str] = None
    status: Optional[str] = None  # e.g., "active", "in maintenance"
    gps_tracker_id: Optional[str] = None

    def __str__(self):
        """Custom string representation."""
        return (
            f"Truck(ID: {self.truck_id}, VIN: {self.vin}, Plate: {self.license_plate_number}, "
            f"Make: {self.truck_make}, Model: {self.truck_model}, Year: {self.truck_year}, "
            f"Type: {self.truck_type}, Status: {self.status}, Assigned Driver ID: {self.assigned_driver_id})"
        )
    