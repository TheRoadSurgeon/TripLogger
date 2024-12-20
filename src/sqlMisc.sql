-- CREATE TABLE IF NOT EXISTS drivers(
--     driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     external_driver_id TEXT,                              -- IE if outside company issue id like FedEx
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL,
--     middle_name TEXT,
--     driver_homebase TEXT,
--     date_of_birth TEXT,                                   -- Store as "YYYY-MM-DD"
--     phone_number TEXT,
--     email TEXT,             
--     photo_url TEXT,
    
--     driver_license_number TEXT,
--     driver_license_state TEXT,        -- e.g. "CA"
--     driver_license_expiration_date TEXT,  -- "YYYY-MM-DD"
--     endorsements TEXT,
    
--     medical_certificate_expiration_date TEXT, -- "YYYY-MM-DD"
    
--     emergency_contact_name TEXT,
--     emergency_contact_phone TEXT,
    
--     created_at TEXT DEFAULT (datetime('now')),
--     updated_at TEXT DEFAULT (datetime('now'))
-- );


-- CREATE TABLE IF NOT EXISTS trucks (
--     truck_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     external_truck_id TEXT,
--     vin TEXT UNIQUE,                -- Vehicle Identification Number
--     license_plate_number TEXT,
--     truck_make TEXT,
--     truck_model TEXT,
--     truck_year INTEGER,             -- e.g., 2020
--     truck_type TEXT,                -- e.g., "tractor", "flatbed"
--     IC_ISP_name TEXT,
--     IC_ISP_number TEXT,
--     color TEXT,
    
--     ownership_status TEXT,          -- e.g., "owned", "leased", "rented"
--     registered_state TEXT,          -- e.g., "CA"
--     registration_expiration_date TEXT, -- "YYYY-MM-DD"
    
--     insurance_policy_number TEXT,
--     insurance_expiration_date TEXT, -- "YYYY-MM-DD"
--     ifta_account_number TEXT,
    
--     odometer_reading REAL,
--     odometer_last_updated_date TEXT, -- "YYYY-MM-DD HH:MM:SS"
    
--     fuel_type TEXT,                -- e.g., "diesel"
--     fuel_efficiency_rating REAL,
--     gvwr TEXT,                     -- Gross Vehicle Weight Rating (store as TEXT or an INTEGER if numeric)
--     cargo_capacity TEXT,
    
--     assigned_driver_id INTEGER,    -- FK to drivers_info(driver_id)
    
--     purchase_date TEXT,            -- "YYYY-MM-DD"
--     warranty_expiration_date TEXT, -- "YYYY-MM-DD"
--     last_service_date TEXT,        -- "YYYY-MM-DD"
--     maintenance_notes TEXT,
--     status TEXT,                   -- e.g., "active", "in maintenance"
--     gps_tracker_id TEXT,
    
--     created_at TEXT DEFAULT (datetime('now')),
--     updated_at TEXT DEFAULT (datetime('now'))
-- );

-- CREATE TABLE IF NOT EXISTS trips (
--     trip_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
--     truck_id INTEGER NOT NULL,                          
--     driver_id INTEGER NOT NULL,
    
--     start_time TEXT,               -- e.g., "YYYY-MM-DD HH:MM:SS"
--     end_time TEXT,                 -- e.g., "YYYY-MM-DD HH:MM:SS"
--     start_location TEXT,           -- e.g., "Bedford Park IL"
--     end_location TEXT,             -- e.g., "Toledo OH"
    
--     location_codes TEXT NOT NULL,       -- JSON for all location codes
--     miles_traveled INTEGER NOT NULL,    -- Total miles traveled
--     roads TEXT NOT NULL,                -- JSON for major roads traveled
    
--     rate REAL,                     -- Per-mile or flat rate for the trip
--     total_payment REAL,            -- Computed: rate * total miles (if applicable)
--     load_description TEXT,         -- Description of cargo/load
--     cargo_weight REAL,             -- Weight of the cargo
--     fuel_used REAL,                -- Fuel consumed (gallons/liters)
    
--     ic_isp_name TEXT,              -- Independent Contractor/Service Provider name if varies by trip
--     ic_isp_number TEXT,            -- IC/ISP identification number if needed
    
--     created_at TEXT DEFAULT (datetime('now')),
--     updated_at TEXT DEFAULT (datetime('now')),
    
--     FOREIGN KEY (truck_id) REFERENCES trucks (truck_id),
--     FOREIGN KEY (driver_id) REFERENCES drivers (driver_id)
-- );


-- INSERT INTO trucks (external_truck_id, odometer_reading, truck_make, truck_model, ic_isp_name, ic_isp_number)
-- VALUES (1, 120000, 'Volvo', 'VLN860', 'Company', 'C12345');

-- INSERT INTO drivers (external_driver_id, first_name, last_name, driver_homebase)
-- VALUES (1001, 'John', 'Doe', '604'),
--        (1002, 'Jane', 'Smith', '436');

-- INSERT INTO Trips (truck_id, driver_id, start_time, location_codes, miles_traveled, roads)
-- VALUES (
--     1, -- Must match an existing TruckID in the Trucks table
--     1, -- Must match an existing DriverID in the Drivers table
--     '2024-12-19',
--     '{"604": "Bedford Park IL", "436": "Toledo OH"}',
--     '{"IL": 30, "IN": 150, "OH": 64}",',
--     '["I-90", "US-294", "I-80"]'
-- );

-- DELETE FROM Trips WHERE TripID >= 10 AND TripID <= 12;

-- ALTER TABLE Trucks ADD COLUMN TruckYear INTEGER;