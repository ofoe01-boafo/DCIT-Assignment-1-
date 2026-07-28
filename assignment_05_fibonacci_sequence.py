# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

#                    SOLUTION
def print_fibonacci_terms(n):
    if n <= 0:
        print("Please enter a positive integer for the number of terms.")
        return
    
    a, b = 0, 1
    fib_sequence = []
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    print(f"Fibonacci sequence: {' '.join(map(str, fib_sequence))}")

def is_fibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    if a == num:
        return True
    else:
        return False

def main():
    # Part A: Print the First N Terms
    while True:
        try:
            n_terms_str = input("How many terms? ")
            n_terms = int(n_terms_str)
            if n_terms > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    print_fibonacci_terms(n_terms)
    
    print("\n" + "="*30 + "\n")

    # Part B: Check if a Number Belongs to the Sequence
    while True:
        try:
            num_to_check_str = input("Enter a number to check: ")
            num_to_check = int(num_to_check_str)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if is_fibonacci(num_to_check):
        print(f"{num_to_check} is a Fibonacci number.")
    else:
        print(f"{num_to_check} is NOT a Fibonacci number.")

if __name__ == "__main__":
    main()