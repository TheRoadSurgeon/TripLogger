-- CREATE TABLE Drivers (
--     DriverID INTEGER PRIMARY KEY NOT NULL,      -- Manually entered unique ID
--     DriverFirstName TEXT NOT NULL,              -- Driver's first name
--     DriverLastName TEXT NOT NULL,               -- Driver's last name
--     DriverHome TEXT                             -- Driver's home location
-- );

-- CREATE TABLE Trucks (
--     TruckID INTEGER PRIMARY KEY NOT NULL,     -- Unique ID for the truck, must be entered manually and cannot be NULL
--     TruckMiles INTEGER DEFAULT 0,             -- Total miles driven by the truck
--     TruckHome TEXT,                           -- Home location of the truck
--     TruckMake TEXT,                           -- Manufacturer of the truck
--     TruckModel TEXT,                          -- Model of the truck
--     IcIspName TEXT,                           -- Name of the Independent Contractor or ISP
--     IcIspNumber TEXT                          -- Contact number of the Independent Contractor or ISP
-- );

-- INSERT INTO Trucks (TruckID, TruckMiles, TruckHome, TruckMake, TruckModel, IcIspName, IcIspNumber)
-- VALUES (1, 120000, '604', 'Volvo', 'VLN860', 'Company', 'C12345');

-- INSERT INTO Drivers (DriverID, DriverFirstName, DriverLastName, DriverHome)
-- VALUES (1001, 'John', 'Doe', '604'),
--        (1002, 'Jane', 'Smith', '436');