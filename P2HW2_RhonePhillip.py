# Phillip Rhone
# Date: 3/15/2026
# Assignment: P2HW2
# Description: Program that stores module grades in a list and
# displays the lowest, highest, sum, and average.

# Pseudocode
# 1. Ask user for 6 module grades
# 2. Store grades in a list
# 3. Use min() to find lowest
# 4. Use max() to find highest
# 5. Use sum() to calculate total
# 6. Calculate average
# 7. Display results formatted

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("\n------------Results------------")

print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")

print("--------------------------------")