"""
Parsing Trip Data Input from Terminal (for now)
"""

def read_trucker_info():
    """
    Reads trucker info
    """
    name = input("Enter your name: ")
    id = input("Enter your trucker ID: ")
    home_base = input("Enter your home base: ")
    return (name, id, home_base)

def read_trip_info():
    """
    Reads trip info
    """
    truck_id = input("Enter ID of Truck for Trip: ")
    day = input("Enter day of trip (mm/dd/yyyy): " )
    start_loc = input("Enter start location: ")
    end_loc = input("Enter end location: ")
    print("Begin entering stops along way; when finished, enter 'x'")
    stops_along_way = []
    user_input = input("Enter Stop: ")
    while user_input != 'x':
        stops_along_way.append(user_input)
    return (truck_id, day, start_loc, end_loc, stops_along_way)
    
if __name__ == "__main__":
    read_trucker_info()
    print("I'm over here")
    