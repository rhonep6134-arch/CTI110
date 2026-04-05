# P4LAB2_RhonePhillip.py

run_again = "yes"

while run_again == "yes":
    
    num = int(input("Enter an integer: "))
    
    # Check if number is negative
    if num < 0:
        print("This program does not handle negative number.")
    
    else:
        # FOR LOOP for multiplication table
        for i in range(1, 13):
            print(num, "*", i, "=", num * i)
    
    # Ask to run again
    run_again = input("Would you like to run the program again? ")
    
print("Exiting program...")