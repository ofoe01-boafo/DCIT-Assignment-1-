// =============================================================================
// PROGRAMMING FUNDAMENTALS — Assignment 4
// =============================================================================
//
// TASK: Matrix Operations
//
// Write a C++ program that performs three operations on matrices (2D arrays),
// each implemented in its own function.
//
// NOTE: Use a fixed maximum size of 10 for array dimensions.
//       Declare arrays as int matrix[10][10].
//
// -----------------------------------------------------------------------------
// PART A — Transpose a Matrix
// -----------------------------------------------------------------------------
// - Read an M x N matrix from the user.
// - Compute and display its transpose (rows become columns, columns become rows).
//
// Example (2 x 3 input):
//
//   Original Matrix:      Transposed Matrix:
//   1  2  3               1  4
//   4  5  6               2  5
//                         3  6
//
// -----------------------------------------------------------------------------
// PART B — Add Two Matrices
// -----------------------------------------------------------------------------
// - Read two matrices of exactly the same size (M x N).
// - Compute their element-wise sum and display the result.
//
// -----------------------------------------------------------------------------
// PART C — Multiply Two Matrices
// -----------------------------------------------------------------------------
// - Read matrix A of size M x N and matrix B of size N x P.
//   (Number of COLUMNS in A must equal number of ROWS in B.)
// - Compute and display the matrix product A x B (result is M x P).
//
// -----------------------------------------------------------------------------
// EXPECTED INPUT FORMAT
// -----------------------------------------------------------------------------
// The user enters each row's values one at a time:
//
//   Enter number of rows: 2
//   Enter number of columns: 3
//   Enter element [0][0]: 1
//   Enter element [0][1]: 2
//   ...
//
// -----------------------------------------------------------------------------
// REQUIREMENTS
// -----------------------------------------------------------------------------
// - Use nested loops for all operations (no external libraries).
// - Each operation must be in its own function (see scaffold below).
// - Display each matrix in a neat, aligned grid using setw().
// - Tip: Complete Part A first, then Parts B and C.
//

// =============================================================================
// YOUR CODE BELOW — remove the // symbols from the scaffold and fill it in
// =============================================================================

//                SOLUTION
#include <iostream>
#include <iomanip>

// Fixed max. size for matrix dimensions
const int MAX_SIZE = 10;

void readMatrix(int matrix[MAX_SIZE][MAX_SIZE], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            std::cout << "Enter element [" << i << "][" << j << "]: ";
            std::cin >> matrix[i][j];
        }
    }
}

void printMatrix(const int matrix[MAX_SIZE][MAX_SIZE], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            std::cout << std::setw(5) << matrix[i][j];
        }
        std::cout << "\n";
    }
}

// Part A: Transpose a Matrix
void transposeMatrix(const int input[MAX_SIZE][MAX_SIZE], int result[MAX_SIZE][MAX_SIZE], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[j][i] = input[i][j];
        }
    }
}

// Part B: Add Two Matrices
void addMatrices(const int A[MAX_SIZE][MAX_SIZE], const int B[MAX_SIZE][MAX_SIZE], int result[MAX_SIZE][MAX_SIZE], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
}

// Part C: Multiply Two Matrices
void multiplyMatrices(const int A[MAX_SIZE][MAX_SIZE], const int B[MAX_SIZE][MAX_SIZE], int result[MAX_SIZE][MAX_SIZE], int rowsA, int colsA, int colsB) {
    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int choice;
    std::cout << "=== MATRIX OPERATIONS MENU ===\n";
    std::cout << "1. Transpose Matrix (Part A)\n";
    std::cout << "2. Add Two Matrices (Part B)\n";
    std::cout << "3. Multiply Two Matrices (Part C)\n";
    std::cout << "Enter your choice (1-3): ";
    std::cin >> choice;

    if (choice == 1) {
        // Part A
        int m, n;
        std::cout << "\n--- PART A: Transpose Matrix ---\n";
        std::cout << "Enter number of rows: ";
        std::cin >> m;
        std::cout << "Enter number of columns: ";
        std::cin >> n;

        int matrix[MAX_SIZE][MAX_SIZE];
        int result[MAX_SIZE][MAX_SIZE];

        readMatrix(matrix, m, n);

        transposeMatrix(matrix, result, m, n);

        std::cout << "\nOriginal Matrix:\n";
        printMatrix(matrix, m, n);

        std::cout << "\nTransposed Matrix:\n";
        printMatrix(result, n, m);

    } else if (choice == 2) {
        // Part B
        int m, n;
        std::cout << "\n--- PART B: Add Two Matrices ---\n";
        std::cout << "Enter number of rows: ";
        std::cin >> m;
        std::cout << "Enter number of columns: ";
        std::cin >> n;

        int A[MAX_SIZE][MAX_SIZE], B[MAX_SIZE][MAX_SIZE], result[MAX_SIZE][MAX_SIZE];

        std::cout << "\nEnter Matrix A elements:\n";
        readMatrix(A, m, n);

        std::cout << "\nEnter Matrix B elements:\n";
        readMatrix(B, m, n);

        addMatrices(A, B, result, m, n);

        std::cout << "\nMatrix Sum (A + B):\n";
        printMatrix(result, m, n);

    } else if (choice == 3) {
        // Part C
        int m, n, p;
        std::cout << "\n--- PART C: Multiply Two Matrices ---\n";
        std::cout << "Enter rows for Matrix A (M): ";
        std::cin >> m;
        std::cout << "Enter cols for Matrix A / rows for Matrix B (N): ";
        std::cin >> n;
        std::cout << "Enter cols for Matrix B (P): ";
        std::cin >> p;

        int A[MAX_SIZE][MAX_SIZE], B[MAX_SIZE][MAX_SIZE], result[MAX_SIZE][MAX_SIZE];

        std::cout << "\nEnter Matrix A (" << m << "x" << n << ") elements:\n";
        readMatrix(A, m, n);

        std::cout << "\nEnter Matrix B (" << n << "x" << p << ") elements:\n";
        readMatrix(B, n, p);

        multiplyMatrices(A, B, result, m, n, p);

        std::cout << "\nMatrix Product (A x B):\n";
        printMatrix(result, m, p);

    } else {
        std::cout << "Invalid choice!\n";
    }

    return 0;
}