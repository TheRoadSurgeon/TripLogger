from .config import db

class Driver(db.Model):
    __tablename__ = 'drivers'
    DriverID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    DOB = db.Column(db.String(10), nullable=False)
    LicenseNumber = db.Column(db.String(50), nullable=False)
    LicenseState = db.Column(db.String(50), nullable=False)
    LicenseExpiration = db.Column(db.String(10), nullable=False)
    LicenseType = db.Column(db.String(50), nullable=False)
    LicenseClass = db.Column