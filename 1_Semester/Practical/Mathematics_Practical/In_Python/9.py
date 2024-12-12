# Check The Diagonalizable Property Of Matrices And Find The Corresponding Eigenvalue And Verify The Cayley- Hamilton Theorem.

import numpy as np
from sympy import Matrix

def check_diagonalizable(matrix):
    sympy_matrix = Matrix(matrix)
    eigenvals = sympy_matrix.eigenvals()
    eigenvectors = sympy_matrix.eigenvects()
    
    if len(eigenvectors) == len(matrix):
        return True, eigenvals, eigenvectors
    else:
        return False, eigenvals, eigenvectors

def verify_cayley_hamilton(matrix):
    sympy_matrix = Matrix(matrix)
    char_poly = sympy_matrix.charpoly()
    characteristic_equation = char_poly.as_expr()
    result = characteristic_equation.subs(sympy_matrix, sympy_matrix)
    if result == 0:
        return True, characteristic_equation
    else:
        return False, characteristic_equation

def main():
    print("Check Diagonalizable Property of Matrix, Eigenvalues, and Verify Cayley-Hamilton Theorem")
    
    print("\nEnter the size of the square matrix (n x n):")
    n = int(input())
    
    print("Enter the matrix row by row, space-separated:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    matrix = np.array(matrix)

    is_diag, eigenvals, eigenvectors = check_diagonalizable(matrix)
    print("\nDiagonalizability Check:")
    if is_diag:
        print("The matrix is diagonalizable.")
        print("Eigenvalues:", eigenvals)
        print("Eigenvectors:")
        for i, eigvec in enumerate(eigenvectors, 1):
            print(f"Eigenvector {i}: {eigvec[2]}")
    else:
        print("The matrix is not diagonalizable.")
    
    is_hamilton, char_eq = verify_cayley_hamilton(matrix)
    print("\nCayley-Hamilton Theorem Verification:")
    if is_hamilton:
        print(f"The matrix satisfies its characteristic equation: {char_eq}")
    else:
        print(f"The matrix does not satisfy its characteristic equation: {char_eq}")

if __name__ == "__main__":
    main()
