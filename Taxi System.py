import random
import datetime
import os

# Fare chart for traveling
fare_chart = {
    "Alvin": {"Alvin": 0, "Jamz": 20, "Razi": 40, "Mali": 40, "Zuhar": 20},
    "Jamz": {"Alvin": 20, "Jamz": 0, "Razi": 20, "Mali": 40, "Zuhar": 40},
    "Razi": {"Alvin": 40, "Jamz": 20, "Razi": 0, "Mali": 20, "Zuhar": 40},
    "Mali": {"Alvin": 40, "Jamz": 40, "Razi": 20, "Mali": 0, "Zuhar": 20},
    "Zuhar": {"Alvin": 20, "Jamz": 40, "Razi": 40, "Mali": 20, "Zuhar": 0}
}

# Vehicle fares
vehicle_fares = {
    "Rickshaw": 1,
    "Car": 2,
    "Van": 3
}

# Generate a random discount amount between 1 and 15 KMD
def generate_random_discount():
    return random.randint(1, 15)

# Calculate the trip fare based on the given start and end cities, and vehicle type
def calculate_trip_fare(start, end, vehicle_type):
    base_fare = fare_chart[start][end]
    fare_multiplier = vehicle_fares[vehicle_type]
    return base_fare * fare_multiplier

# Generate an invoice file for the trip
def generate_invoice(start, end, fare, promo, random_discount, final_payment):
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H_%M_%S_%f")
    timestamp = f"{date} {time}"

    invoice = f"invoice issuing date: {date}\nTime of creating invoice: {time}\nStarting city: {start}\nEnding City: {end}\nTotal Fare of trip: {fare} KMD\nPromo Applied: {promo} KMD\nRandom Discount: {random_discount} KMD\nFinal Payment: {final_payment} KMD"

    # Determine the desktop path and create a directory named "TravelInvoices" if it doesn't exist
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    directory_path = os.path.join(desktop_path, "TravelInvoices")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_name = os.path.join(directory_path, f"{timestamp}.txt")

    with open(file_name, "w") as file:
        file.write(invoice)

    print("Invoice generated successfully.")
    return file_name

# Show the fare table for traveling between cities
def show_fare_table():
    print("\nFare Table for Traveling Between Cities:")
    cities = list(fare_chart.keys())
    print("".ljust(10), end="")
    for city in cities:
        print(city.ljust(10), end="")
    print()
    for start_city in cities:
        print(start_city.ljust(10), end="")
        for end_city in cities:
            print(str(fare_chart[start_city][end_city]).ljust(10), end="")
        print()

# Show the vehicle fares
def show_vehicle_fares():
    print("\nVehicle Fares:")
    print("Vehicle Type".ljust(15), "Fare Multiplier")
    for vehicle, fare in vehicle_fares.items():
        print(vehicle.ljust(15), str(fare))

# Show help information for the 'dm' command
def show_help():
    print("Commands:")
    print("dm [start_city] [end_city] - Shows the fare between two cities and generates an invoice file for the trip.")
    print("dm [start_city] [end_city] /promo[amount] - Shows the fare between two cities after applying a promotional code.")
    print("dm [start_city] [end_city] /car - Shows the fare between two cities and generates an invoice file for the trip using a car.")
    print("dm [start_city] [end_city] /promo[amount] /van - Shows the fare between two cities while applying a discount to the total bill and using a van.")
    print("dm /? - Show how the 'dm' command functions.")

# Show the fare table and vehicle fares when the program starts
show_fare_table()
show_vehicle_fares()

# Main loop
while True:
    command = input("\nEnter a dm command: ")

    if command.lower() == "exit":
        break

    if command.startswith("dm"):
        command_parts = command.split()[1:]
        if len(command_parts) >= 2:
            # Capitalize the city names for consistency with the fare_chart keys
            start_city = command_parts[0].capitalize()
            end_city = command_parts[1].capitalize()

            file_name = generate_invoice(start_city, end_city, 0, 0, 0, 0)  # Pass placeholders for unused arguments
            if file_name:
                print(f"Invoice generated successfully. File saved at: {file_name}")
        else:
            print("Invalid command. Please provide at least two city names.")
    elif command == "dm /?":
        show_help()
    else:
        print("Invalid command. Please try again or enter 'dm /?' for help.")
