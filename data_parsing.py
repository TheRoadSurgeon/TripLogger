"""
Parsing Trip Data Input from Terminal (for now)
"""
from enum import Enum


def read_trucker_info() -> dict[str, int, int]:
    """
    Reads trucker info
    """
    name = input("Enter your name: ")
    id = input("Enter your trucker ID: ")
    home_base = input("Enter your home base: ")
    return {"name": name, "id": id, "home base": home_base}


if __name__ == "__main__":
    read_trucker_info()
    print("I'm over here")
