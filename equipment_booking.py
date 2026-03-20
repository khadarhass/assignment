"""
Bright Minds Academy - Equipment Booking System

Simple menu-driven console program for managing equipment bookings.
This version is kept beginner-friendly for a university assignment.
"""

from datetime import datetime


def parse_date(date_text):
    """Parse and validate a date in YYYY-MM-DD format."""
    try:
        parsed = datetime.strptime(date_text, "%Y-%m-%d")
        return parsed.date()
    except ValueError:
        return None


def normalize_equipment_name(name):
    """Normalise equipment names for consistent dictionary keys."""
    return " ".join(name.strip().lower().split())


def seed_default_equipment():
    """Create starter equipment records."""
    defaults = ["Laptop 1", "Laptop 2", "Projector A", "Tablet 1"]
    equipment = {}
    for item in defaults:
        key = normalize_equipment_name(item)
        equipment[key] = {
            "display_name": item,
            "bookings": [],
        }
    return equipment


def add_equipment(equipment_db):
    """Add a new equipment item to the system."""
    print("\n--- Add New Equipment ---")
    display_name = input("Enter equipment name: ").strip()

    if not display_name:
        print("Error: Equipment name cannot be empty.")
        return

    equipment_key = normalize_equipment_name(display_name)
    if equipment_key in equipment_db:
        print("Error: That equipment already exists.")
        return

    equipment_db[equipment_key] = {
        "display_name": display_name,
        "bookings": [],
    }
    print(f"Success: '{display_name}' was added.")


def is_equipment_available(equipment_db, equipment_key, booking_date):
    """Check if an equipment item is free on a date."""
    bookings = equipment_db[equipment_key]["bookings"]
    for booking in bookings:
        if booking["booking_date"] == booking_date:
            return False
    return True


def record_booking(equipment_db):
    """Record a booking for an equipment item."""
    print("\n--- Record a Booking ---")
    student_name = input("Enter student name: ").strip()
    equipment_name = input("Enter equipment name: ").strip()
    date_text = input("Enter booking date (YYYY-MM-DD): ").strip()

    if not student_name:
        print("Error: Student name cannot be empty.")
        return

    if not equipment_name:
        print("Error: Equipment name cannot be empty.")
        return

    parsed_date = parse_date(date_text)
    if parsed_date is None:
        print("Error: Invalid date. Please use YYYY-MM-DD format.")
        return

    equipment_key = normalize_equipment_name(equipment_name)
    if equipment_key not in equipment_db:
        print("Error: Equipment not found.")
        return

    booking_date = parsed_date.isoformat()
    if not is_equipment_available(equipment_db, equipment_key, booking_date):
        print("Error: This equipment is already booked on that date.")
        return

    equipment_db[equipment_key]["bookings"].append(
        {
            "student_name": student_name,
            "booking_date": booking_date,
        }
    )
    print("Success: Booking recorded.")


def view_bookings(equipment_db):
    """Display all booking records."""
    print("\n--- Booking Records ---")

    if not equipment_db:
        print("No equipment found.")
        return

    for equipment_key in sorted(equipment_db.keys()):
        item = equipment_db[equipment_key]
        print(f"\nEquipment: {item['display_name']}")
        if not item["bookings"]:
            print("  No bookings yet.")
        else:
            for index, booking in enumerate(item["bookings"], start=1):
                print(
                    f"  {index}. Student: {booking['student_name']} | Date: {booking['booking_date']}"
                )


def search_bookings(equipment_db):
    """Search bookings by partial student name or equipment name."""
    print("\n--- Search Bookings ---")
    search_text = input("Enter student or equipment name to search: ").strip().lower()

    if not search_text:
        print("Error: Search text cannot be empty.")
        return

    found_any = False

    for equipment_key in sorted(equipment_db.keys()):
        item = equipment_db[equipment_key]
        equipment_match = search_text in item["display_name"].lower()

        for booking in item["bookings"]:
            student_match = search_text in booking["student_name"].lower()
            if equipment_match or student_match:
                if not found_any:
                    print("\nResults:")
                found_any = True
                print(
                    f"- Equipment: {item['display_name']} | "
                    f"Student: {booking['student_name']} | "
                    f"Date: {booking['booking_date']}"
                )

    if not found_any:
        print("No matching bookings found.")


def print_menu():
    """Display the main menu options."""
    print("\n=== Bright Minds Academy Equipment Booking System ===")
    print("1. Add new equipment")
    print("2. Record a booking")
    print("3. View booking records")
    print("4. Search bookings")
    print("5. Exit")


def main_menu_loop():
    """Run the menu loop until the user exits."""
    equipment_db = seed_default_equipment()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_equipment(equipment_db)
        elif choice == "2":
            record_booking(equipment_db)
        elif choice == "3":
            view_bookings(equipment_db)
        elif choice == "4":
            search_bookings(equipment_db)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid menu option. Please choose 1 to 5.")


if __name__ == "__main__":
    main_menu_loop()
