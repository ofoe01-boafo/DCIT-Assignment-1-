// =============================================================================
// PROGRAMMING FUNDAMENTALS — Assignment 3
// =============================================================================
//
// TASK: Array Statistics Calculator
//
// Write a C++ program that reads a collection of numbers from the user
// and computes key statistical values using separate functions.
//
// -----------------------------------------------------------------------------
// EXPECTED INPUT / OUTPUT EXAMPLE
// -----------------------------------------------------------------------------
//
//   How many numbers? 5
//   Enter number 1: 4
//   Enter number 2: 7
//   Enter number 3: 2
//   Enter number 4: 9
//   Enter number 5: 1
//
//   Results:
//   Sum:     23
//   Average: 4.6
//   Maximum: 9
//   Minimum: 1
//
// -----------------------------------------------------------------------------
// REQUIREMENTS
// -----------------------------------------------------------------------------
// - You MUST implement each calculation in its own function (see scaffold).
// - You may NOT use any standard library functions like accumulate(), max(),
//   or min(). Implement the logic yourself using loops.
// - N must be a positive integer. If the user enters 0 or a negative number,
//   print an error message and stop.
//

//
// =============================================================================
// YOUR CODE BELOW — remove the // symbols from the scaffold and fill it in
// =============================================================================

//                    SOLUTION
#include <iostream>
#include <vector>

double calculateSum(const std::vector<double>& numbers) {
    double total = 0.0;
    for (double num : numbers) {
        total += num;
    }
    return total;
}

double calculateAverage(const std::vector<double>& numbers) {
    if (numbers.empty()) return 0.0;
    return calculateSum(numbers) / numbers.size();
}

double calculateMax(const std::vector<double>& numbers) {
    double maxVal = numbers[0];
    for (size_t i = 1; i < numbers.size(); ++i) {
        if (numbers[i] > maxVal) {
            maxVal = numbers[i];
        }
    }
    return maxVal;
}

double calculateMin(const std::vector<double>& numbers) {
    double minVal = numbers[0];
    for (size_t i = 1; i < numbers.size(); ++i) {
        if (numbers[i] < minVal) {
            minVal = numbers[i];
        }
    }
    return minVal;
}

int main() {
    int count = 0;
    std::cout << "How many numbers? ";
    std::cin >> count;

    if (count <= 0) {
        std::cout << "Please enter a number greater than 0.\n";
        return 0;
    }

    std::vector<double> numbers(count);
    for (int i = 0; i < count; ++i) {
        std::cout << "Enter number " << (i + 1) << ": ";
        std::cin >> numbers[i];
    }

    std::cout << "\nResults:\n";
    std::cout << "Sum:     " << calculateSum(numbers) << "\n";
    std::cout << "Average: " << calculateAverage(numbers) << "\n";
    std::cout << "Maximum: " << calculateMax(numbers) << "\n";
    std::cout << "Minimum: " << calculateMin(numbers) << "\n";

    return 0;
}