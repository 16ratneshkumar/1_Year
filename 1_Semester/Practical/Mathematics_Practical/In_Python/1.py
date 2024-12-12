# Create And Transform Vectors And Matrices (The Transpose Vector (Matrix) Conjugate Transpose Of A Vector (Matrix)).

import numpy as np

def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements row by row (use space to separate numbers, e.g., '1+2j 3+4j'):")

    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        matrix.append([complex(num) if 'j' in num else float(num) for num in row])
    
    return np.array(matrix)

def main():
    print("Choose an operation:")
    print("1. Vector")
    print("2. Matrix")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        vector = input("Enter the vector elements separated by spaces (e.g., '1+2j 3+4j 5+6j'): ").split()
        vector = np.array([complex(num) if 'j' in num else float(num) for num in vector])
        print("\nOriginal Vector:")
        print(vector)

        print("\nTranspose of the Vector:")
        print(np.transpose(vector)) 
        print("\nConjugate Transpose of the Vector:")
        print(np.conjugate(vector))

    elif choice == 2:
        matrix = get_matrix_input()
        print("\nOriginal Matrix:")
        print(matrix)

        print("\nTranspose of the Matrix:")
        print(np.transpose(matrix))
        print("\nConjugate Transpose of the Matrix:")
        print(np.conjugate(np.transpose(matrix)))

    else:
        print("Invalid choice! Please choose 1 or 2.")

if __name__ == "__main__":
    main()
