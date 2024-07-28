## Trip Fare Calculator

### Description
The Trip Fare Calculator is a Python application designed to calculate and generate invoices for trips between cities using different types of vehicles. It allows users to view fare charts, vehicle fare multipliers, apply random discounts, and create invoices for trips.

### Features
- **Fare Calculation**: Calculate trip fare based on starting and ending cities, and vehicle type.
- **Discount Application**: Apply a random discount to the trip fare.
- **Invoice Generation**: Generate and save an invoice for the trip on the desktop.
- **Fare and Vehicle Information**: Display fare chart between cities and vehicle fare multipliers.

### How to Use
1. **Run the Program**: Execute the script to start the application.
   ```sh
   python trip_fare_calculator.py
   ```
2. **View Fare Chart and Vehicle Fares**: The fare chart and vehicle fares will be displayed when the program starts.
3. **Enter Commands**: Use commands to calculate fares, apply promotions, and generate invoices.

### Example Usage
1. **Calculate Fare and Generate Invoice**: 
   ```sh
   dm Alvin Jamz
   ```
   This will calculate the fare between Alvin and Jamz using a Rickshaw and generate an invoice.
2. **Apply Promotion**: 
   ```sh
   dm Alvin Jamz /promo5
   ```
   This will calculate the fare between Alvin and Jamz, apply a 5 KMD promotional discount, and generate an invoice.
3. **Use Specific Vehicle**: 
   ```sh
   dm Alvin Jamz /car
   ```
   This will calculate the fare between Alvin and Jamz using a Car and generate an invoice.

### Invoice Generation
The program generates an invoice file with details about the trip, fare, discounts, and final payment. The invoice is saved on the desktop in a directory named `TravelInvoices`.

### Author
Nuran.

### License
This project is licensed under the MIT License.
