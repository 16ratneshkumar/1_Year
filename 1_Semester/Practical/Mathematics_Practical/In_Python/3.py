# Find Cofactors, Determinant, Adjoint And Inverse Of A Matrix.

from sympy import Matrix, symbols

def get_square_matrix():
    size = int(input("Enter the size of the square matrix (e.g., 3 for a 3x3 matrix): "))
    print(f"Enter the elements row by row (use space to separate numbers):")

    matrix = []
    for i in range(size):
        row = input(f"Enter row {i + 1}: ").split()
        matrix.append([int(num) for num in row])
    
    return Matrix(matrix)

def main():
    print("Matrix Operations: Cofactors, Determinant, Adjoint, and Inverse")
    matrix = get_square_matrix()

    print("\nOriginal Matrix:")
    print(matrix)

    determinant = matrix.det()
    print("\nDeterminant of the Matrix:")
    print(determinant)

    if determinant == 0:
        print("\nThe matrix is singular and does not have an inverse.")
    else:
        cofactors = matrix.cofactor_matrix()
        print("\nCofactor Matrix:")
        print(cofactors)

        adjoint = cofactors.transpose()
        print("\nAdjoint of the Matrix:")
        print(adjoint)

        inverse = matrix.inv()
        print("\nInverse of the Matrix:")
        print(inverse)

if __name__ == "__main__":
    main()
