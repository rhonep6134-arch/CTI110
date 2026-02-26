# Name: Phillip Rhone
# Date: 2026-02-26
# Assignment Name: P1HW1
# Description: Collects user input to calculate exponents and perform addition/subtraction.

print("----Calculating Exponents----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

power_result = base ** exponent
print()
print(f"{base} raised to the power of {exponent} is {power_result} !!")
print()

print("----Addition and Subtraction----")
print()

start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))

final_result = start_num + add_num - sub_num
print()
print(f"{start_num} + {add_num} - {sub_num} is equal to {final_result}")