# Name: Phillip Justin Rhone
# Date: 2026-02-26
# Assignment Name: P1HW2
# Description: Calculates and displays travel expenses and remaining budget.

# Pseudocode:
# 1. Ask user for travel budget
# 2. Ask user for travel destination
# 3. Ask user for gas expense
# 4. Ask user for accommodation expense
# 5. Ask user for food expense
# 6. Add all expenses
# 7. Subtract expenses from budget
# 8. Display formatted results

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print()
print("----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print()
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print()
print(f"Remaining Balance: ${remaining_balance:.2f}")