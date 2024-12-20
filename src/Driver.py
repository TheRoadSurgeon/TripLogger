"""
Date: 12/18/2024
@author Hristian Tountchev
A class file that creates driver details
"""
from dataclasses import dataclass, field
from typing import Optional

# Class that keeps driver information nice an neat.
@dataclass
class Driver:
    driver_id: Optional[int] = None
    external_driver_id: Optional[str] = None
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    driver_homebase: Optional[str] = None
    date_of_birth: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    photo_url: Optional[str] = None

    driver_license_number: Optional[str] = None
    driver_license_state: Optional[str] = None
    driver_licence_expiration: Optional[str] = None
    endorsement: Optional[str] = None

    medical_card_expiration: Optional[str] = None

    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None


    def __str__(self):
        """Custom string representation."""
        return (
            f"Driver(ID: {self.driver_id}, Name: {self.first_name} {self.last_name}, "
            f"Home Base: {self.driver_homebase}, DOB: {self.date_of_birth}, "
            f"License: {self.driver_license_number} ({self.driver_license_state}), "
            f"Phone: {self.phone_number}, Email: {self.email})"
        )
    
    

