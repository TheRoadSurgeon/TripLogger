PRAGMA foreign_keys = ON;

INSERT INTO Trips (TruckID, DriverID, Date, LocationCodes, MilesTraveled, Roads)
VALUES (
    1, -- Must match an existing TruckID in the Trucks table
    1002, -- Must match an existing DriverID in the Drivers table
    '12-19-2024 2:30',
    '{"604": "Bedford Park IL", "436": "Toledo OH"}',
    '{"604": 30, "436": 150}',
    '["I-90", "US-294", "I-80"]'
);


