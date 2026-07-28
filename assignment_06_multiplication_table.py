# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


#                    SOLUTION
def print_single_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

def print_all_multiplication_tables(n):
    for num in range(1, n + 1):
        print_single_multiplication_table(num)
        if num < n:
            print("-----------")

def main():
    # Part A: Single Table
    while True:
        try:
            num_str = input("Enter a number to display its multiplication table: ")
            number_to_display = int(num_str)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    print_single_multiplication_table(number_to_display)
    
    print("\n" + "="*30 + "\n")

    # Part B: Tables from 1 to N
    while True:
        try:
            n_str = input("Enter a number N to display multiplication tables from 1 to N: ")
            n_limit = int(n_str)
            if n_limit > 0:
                break
            else:
                print("Please enter a positive integer for N.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print_all_multiplication_tables(n_limit)

if __name__ == "__main__":
    main()