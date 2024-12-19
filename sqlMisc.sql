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

-- CREATE TABLE Trips (
--     TripID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, -- Auto-incremented unique trip identifier
--     TruckID INTEGER NOT NULL,                          -- Foreign key referencing Trucks table
--     DriverID INTEGER NOT NULL,                         -- Foreign key referencing Drivers table
--     Date TEXT NOT NULL,                                -- Date and time of the trip (MM-DD-YYYY H:M format)
--     LocationCodes TEXT NOT NULL,                       -- JSON string storing location codes (e.g., {"604": "Bedford Park IL", "436": "Toledo OH"})
--     MilesTraveled TEXT NOT NULL,                       -- JSON string storing miles traveled (e.g., {"604": 30, "436": 150})
--     Roads TEXT NOT NULL,                               -- JSON string storing major roads traveled (e.g., ["I-90", "US-41"]),
--     FOREIGN KEY (TruckID) REFERENCES Trucks (TruckID), -- Establish TruckID as a foreign key
--     FOREIGN KEY (DriverID) REFERENCES Drivers (DriverID) -- Establish DriverID as a foreign key
-- );

-- INSERT INTO Trucks (TruckID, TruckMiles, TruckHome, TruckMake, TruckModel, IcIspName, IcIspNumber)
-- VALUES (1, 120000, '604', 'Volvo', 'VLN860', 'Company', 'C12345');

-- INSERT INTO Drivers (DriverID, DriverFirstName, DriverLastName, DriverHome)
-- VALUES (1001, 'John', 'Doe', '604'),
--        (1002, 'Jane', 'Smith', '436');

-- INSERT INTO Trips (TruckID, DriverID, Date, LocationCodes, MilesTraveled, Roads)
-- VALUES (
--     11, -- Must match an existing TruckID in the Trucks table
--     1, -- Must match an existing DriverID in the Drivers table
--     '12-18-2024 14:30',
--     '{"604": "Bedford Park IL", "436": "Toledo OH"}',
--     '{"604": 30, "436": 150}',
--     '["I-90", "US-41"]'
-- );

-- DELETE FROM Trips WHERE TripID >= 10 AND TripID <= 12;