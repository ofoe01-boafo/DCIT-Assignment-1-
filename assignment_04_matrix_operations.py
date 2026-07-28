# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# ============================================
# PROGRAMMING FUNDAMENTALS - Assignment 4
# Matrix Operations
# ============================================

def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# PART A - Transpose

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# PART B - Matrix Addition

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# PART C - Matrix Multiplication

def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


# MAIN PROGRAM

# -------- PART A --------
print("\n Part A - TRANSPOSE MATRIX ")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
print_matrix(matrix)

print("\nTransposed Matrix:")
print_matrix(transpose_matrix(matrix))


# ---------- PART B ----------
print("\n Part B - ADD TWO MATRICES ")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A")
matrix_a = read_matrix(rows, cols)

print("\nEnter Matrix B")
matrix_b = read_matrix(rows, cols)

print("\nMatrix A:")
print_matrix(matrix_a)

print("\nMatrix B:")
print_matrix(matrix_b)

print("\nSum of Matrices:")
print_matrix(add_matrices(matrix_a, matrix_b))


# ---------- PART C ----------
print("\n Part C - MULTIPLY TWO MATRICES ")

rows_a = int(input("Enter number of rows for Matrix A: "))
cols_a = int(input("Enter number of columns for Matrix A: "))

print("\nEnter Matrix A")
matrix_a = read_matrix(rows_a, cols_a)

rows_b = int(input("\nEnter number of rows for Matrix B: "))
cols_b = int(input("Enter number of columns for Matrix B: "))

if cols_a != rows_b:
    print("\nMatrix multiplication is not possible.")
    print("Columns of Matrix A must equal rows of Matrix B.")
else:
    print("\nEnter Matrix B")
    matrix_b = read_matrix(rows_b, cols_b)

    print("\nMatrix A:")
    print_matrix(matrix_a)

    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nProduct Matrix:")
    print_matrix(multiply_matrices(matrix_a, matrix_b))