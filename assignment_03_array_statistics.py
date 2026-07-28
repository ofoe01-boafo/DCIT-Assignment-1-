# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
#                     SOLUTION

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    if not numbers:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None  
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def find_minimum(numbers): 
    if not numbers:
        return None 
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# --- Main program ---
numbers_list = []

while True:
    try:
        num_count_str = input("How many numbers? ")
        n = int(num_count_str)
        if n <= 0:
            print("Error: Please enter a positive integer for the number of inputs.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for i in range(1, n + 1):
    while True:
        try:
            num_str = input(f"Enter number {i}: ")
            number = int(num_str)
            numbers_list.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

sum_result = calculate_sum(numbers_list)
average_result = calculate_average(numbers_list)
max_result = find_maximum(numbers_list)
min_result = find_minimum(numbers_list)

print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Average: {average_result}")
print(f"Maximum: {max_result}")
print(f"Minimum: {min_result}")