# Name: Phillip Rhone
# Date: 3/29/2026
# Assignment: P3HW2 Salary
# Description: Calculates employee pay including overtime and displays formatted output.

# Pseudocode:
# 1. Get employee name
# 2. Get hours worked
# 3. Get pay rate
# 4. If hours > 40:
#       overtime = hours - 40
#       overtime pay = overtime * rate * 1.5
#       regular pay = 40 * rate
#    Else:
#       overtime = 0
#       overtime pay = 0
#       regular pay = hours * rate
# 5. gross pay = regular pay + overtime pay
# 6. Display everything formatted

# User input
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

print("--------------------------------------")

# Overtime logic
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    regular_pay = 40 * rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours * rate

# Gross pay
gross_pay = regular_pay + overtime_pay

# Output
print(f"Employee name: {name}")
print()

print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<15}{'Gross Pay'}")
print("------------------------------------------------------------------------------------------")

print(f"{hours:<15.1f}{rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<14.2f}${gross_pay:.2f}")