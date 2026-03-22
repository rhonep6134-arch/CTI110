# P3LAB_RhonePhillip
# Description: This program calculates the most efficient number of dollars,
# quarters, dimes, nickels, and pennies for a given amount of money.

# Get user input
amount = float(input("Enter the amount of money as a float: ").replace("$", ""))

# Convert to cents
cents = int(round(amount * 100))

# Handle no change case
if cents == 0:
    print("No change")
else:
    # Calculate each denomination
    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    # Output results
    if dollars > 0:
        print(f"{dollars} Dollar" if dollars == 1 else f"{dollars} Dollars")

    if quarters > 0:
        print(f"{quarters} Quarter" if quarters == 1 else f"{quarters} Quarters")

    if dimes > 0:
        print(f"{dimes} Dime" if dimes == 1 else f"{dimes} Dimes")

    if nickels > 0:
        print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")

    if pennies > 0:
        print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")