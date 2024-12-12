# Generate The Matrix Into Echelon Form And Find Its Rank.

import numpy as np
from sympy import Matrix

def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements row by row (use space to separate numbers, e.g., '1 2 3'):")

    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        matrix.append([float(num) for num in row])
    
    return np.array(matrix)

def row_echelon_and_rank(matrix):
    sympy_matrix = Matrix(matrix)
    
    echelon_matrix = sympy_matrix.rref()[0] 
    print("\nRow Echelon Form (REF):")
    print(np.array(echelon_matrix, dtype=float)) 
    
    rank = sympy_matrix.rank()
    print("\nRank of the Matrix:")
    print(rank)

def main():
    print("Generate a Matrix into Echelon Form and Find its Rank")
    matrix = get_matrix_input()

    print("\nOriginal Matrix:")
    print(matrix)

    row_echelon_and_rank(matrix)

if __name__ == "__main__":
    main()
