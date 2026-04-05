# Phillip Rhone
# Date: 3/8/2026
# Assignment: P2LAB2
# This program stores vehicle MPG values in a dictionary and
# calculates how many gallons of gas are needed for a trip.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()
print(keys)

car = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[car]

print(f"\nThe {car} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {car}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {car} {miles:.1f} miles.")