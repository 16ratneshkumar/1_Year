# Generate Basis Of Column Space, Null Space, Row Space And Left Null Space Of A Matrix Space.

import numpy as np
from sympy import Matrix

def compute_spaces(matrix):
    sympy_matrix = Matrix(matrix)

    col_space = sympy_matrix.columnspace()
    col_basis = [np.array(col).astype(float).flatten() for col in col_space]

    null_space = sympy_matrix.nullspace()
    null_basis = [np.array(null).astype(float).flatten() for null in null_space]

    row_space = sympy_matrix.rowspace()
    row_basis = [np.array(row).astype(float).flatten() for row in row_space]

    left_null_space = sympy_matrix.T.nullspace()
    left_null_basis = [np.array(left_null).astype(float).flatten() for left_null in left_null_space]

    return col_basis, null_basis, row_basis, left_null_basis

def display_basis(name, basis):
    print(f"\nBasis of {name}:")
    if len(basis) == 0:
        print("No basis (zero-dimensional space)")
    else:
        for i, vec in enumerate(basis, 1):
            print(f"Vector {i}: {vec}")

def main():
    print("Generate Basis of Column Space, Null Space, Row Space, and Left Null Space of a Matrix")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter the matrix row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    matrix = np.array(matrix)

    col_basis, null_basis, row_basis, left_null_basis = compute_spaces(matrix)

    display_basis("Column Space", col_basis)
    display_basis("Null Space", null_basis)
    display_basis("Row Space", row_basis)
    display_basis("Left Null Space", left_null_basis)

if __name__ == "__main__":
    main()
